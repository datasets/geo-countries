.PHONY: data clean
clean:
	find . -maxdepth 1 -name "*.zip" -exec rm -f {} +

download:
	if [ ! -f ne_10m_admin_0_countries.zip ]; then curl -L -o ne_10m_admin_0_countries.zip https://naciscdn.org/naturalearth/10m/cultural/ne_10m_admin_0_countries.zip; fi

data: download
	# Natural Earth uses -99 for France and Norway; fill them from its *_EH fields (FRA/FR, NOR/NO).
	ogr2ogr -f GeoJSON -makevalid -lco COORDINATE_PRECISION=6 -dialect SQLite -nln ne_10m_admin_0_countries -sql "SELECT admin AS name, CASE WHEN iso_a3 = '-99' AND adm0_a3 IN ('FRA','NOR') THEN iso_a3_eh ELSE iso_a3 END AS \"ISO3166-1-Alpha-3\", CASE WHEN iso_a2 = '-99' AND adm0_a3 IN ('FRA','NOR') THEN iso_a2_eh ELSE iso_a2 END AS \"ISO3166-1-Alpha-2\", geometry FROM ne_10m_admin_0_countries" data/countries.geojson /vsizip/ne_10m_admin_0_countries.zip