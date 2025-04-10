.PHONY: data clean
clean:
	find . -maxdepth 1 -name "*.zip" -exec rm -f {} +

download:
	if [ ! -f ne_10m_admin_0_countries.zip ]; then curl -L -o ne_10m_admin_0_countries.zip https://naciscdn.org/naturalearth/10m/cultural/ne_10m_admin_0_countries.zip; fi

data: download
	ogr2ogr -f GeoJSON -makevalid -lco COORDINATE_PRECISION=6 -sql "SELECT admin as name, iso_a3 as \"ISO3166-1-Alpha-3\", iso_a2 as \"ISO3166-1-Alpha-2\" FROM ne_10m_admin_0_countries" data/countries.geojson /vsizip/ne_10m_admin_0_countries.zip