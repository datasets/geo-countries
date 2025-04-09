## Description

These scripts retrieve data from Natural Earth's website and compute the ``data/countries.geojson`` file.


## Install the dependencies

The scripts make use of the wonderful ogr2ogr tool (part of the gdal suite) and a few other shell commands that are glued together with selenium parser.
Therefore, you'll need to install [git](https://git-scm.com/downloads), [gdal](https://gdal.org/en/latest/download.html)


	
## Run the scripts

Make sure the ogr2ogr tool is available on command line.

After you have checked out the code, go into the script directory and run the processing :
	
    # Install libraries
    pip install -r scripts/requirements.txt

    # Run the job locally through Makefile
    make data
    
    # or else you could run scripts manually
    python3 scripts/process.py
