import os
import time
import subprocess

from zipfile import ZipFile 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Get the current directory where the script is running
current_directory = os.getcwd()
zip_file_name = 'ne_10m_admin_0_countries.zip'

# Directory where the ZIP file will be extracted
extract_to_directory = os.path.join(current_directory, 'extracted_files')

# Path where the final GeoJSON file will be placed
geojson_name = 'ne_10m_admin_0_countries.geojson'
data_directory_name = 'data'
countries_geojson_name = 'countries.geojson'

chrome_options = webdriver.ChromeOptions()
prefs = {"download.default_directory": current_directory,  # Set the download folder to the current working directory
         "download.prompt_for_download": False,  # Disable the prompt
         "safebrowsing.enabled": True}  # Enable safe browsing
chrome_options.add_experimental_option("prefs", prefs)

def download_file():
    driver = webdriver.Chrome(options=chrome_options)
    driver.get('https://www.naturalearthdata.com/downloads/10m-cultural-vectors/10m-admin-0-countries/')

    try:
        download_link = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'download-link'))
        )
        download_link.click()

        time.sleep(10)  # Wait for the file to download (adjust as necessary)

        print(f"File downloaded successfully in {current_directory}")
    except Exception as e:
        print(f"Error occurred: {e}")
    finally:
        driver.quit()

def unzip_file():
    """Extract the downloaded ZIP file to the extracted_files directory."""
    zip_file_path = os.path.join(current_directory, zip_file_name)

    # Create the extracted_files directory if it doesn't exist
    if not os.path.exists(extract_to_directory):
        os.makedirs(extract_to_directory)

    # Extract the ZIP file contents
    with ZipFile(zip_file_path, 'r') as zObject:
        zObject.extractall(path=extract_to_directory)

    print(f"Files extracted to {extract_to_directory}")

def convert_to_geojson():
    """Converts the shapefile to GeoJSON using ogr2ogr."""
    # Define the paths to the necessary shapefile components
    shp_path = os.path.join(extract_to_directory, 'ne_10m_admin_0_countries.shp')
    geojson_path = os.path.join(extract_to_directory, geojson_name)

    # Run ogr2ogr to convert shapefile to GeoJSON
    command = [
        'ogr2ogr', '-select', 'admin,iso_a3', '-f', 'GeoJSON', 
        geojson_path, shp_path
    ]
    subprocess.run(command, check=True)

    print(f"Converted shapefile to GeoJSON: {geojson_path}")

def create_data_directory():
    """Creates a new directory in the parent directory called 'data'."""
    parent_directory = os.path.abspath(os.path.join(current_directory, '..'))
    data_directory = os.path.join(parent_directory, data_directory_name)

    # Create the directory if it doesn't exist
    if not os.path.exists(data_directory):
        os.makedirs(data_directory)

    print(f"Created data directory at {data_directory}")
    return data_directory

def rename_geojson_fields():
    """Renames fields in the GeoJSON file and moves it to the '../data' directory."""
    geojson_path = os.path.join(extract_to_directory, geojson_name)

    # Get the destination directory and path for the renamed GeoJSON
    data_directory = create_data_directory()
    new_geojson_path = os.path.join(data_directory, countries_geojson_name)

    # Perform field renaming by reading the file, replacing text, and writing it back
    with open(geojson_path, 'r') as f:
        content = f.read()

    # Replace the fields in the GeoJSON content
    content = content.replace('"admin": ', '"name": ')
    content = content.replace('"iso_a3": ', '"ISO3166-1-Alpha-3": ')

    # Write the updated content to the new file
    with open(new_geojson_path, 'w') as f:
        f.write(content)

    print(f"Renamed fields and moved GeoJSON to {new_geojson_path}")

if __name__ == '__main__':
    download_file()       # Step 1: Download the ZIP file
    unzip_file()          # Step 2: Unzip the downloaded file
    convert_to_geojson()  # Step 3: Convert shapefile to GeoJSON
    rename_geojson_fields()  # Step 4: Rename fields and save to ../data/countries.geojson
