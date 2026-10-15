<a className="gh-badge" href="https://datahub.io/core/geo-countries"><img src="https://badgen.net/badge/icon/View%20on%20datahub.io/orange?icon=https://datahub.io/datahub-cube-badge-icon.svg&label&scale=1.25" alt="badge" /></a>

# Country Polygons as GeoJSON

GeoJSON polygons for the world's countries and for some territories, disputed areas and special areas, taken from Natural Earth. Each polygon carries the country name and its ISO 3166-1 alpha-2 and alpha-3 codes.

Column definitions and types are in `datapackage.json`.

## Data

`data/countries.geojson` is one GeoJSON `FeatureCollection`. Each feature is one country or area, as a `Polygon` or `MultiPolygon`, with three properties:

| Property | Meaning |
|---|---|
| `name` | Common name of the country or area, for example `Argentina` or `Kosovo` |
| `ISO3166-1-Alpha-3` | 3-letter ISO 3166-1 country code, for example `ARG`. `-99` where there is no ISO code |
| `ISO3166-1-Alpha-2` | 2-letter ISO 3166-1 country code, for example `AR`. `-99` where there is no ISO code |

More information about each country is in the [country-codes][country-codes] data package. Join it on `ISO3166-1-Alpha-3`.

### Known limitations

* Natural Earth writes `-99` where it has no ISO code in its main code fields. Two real countries are affected, France and Norway. The build fills them from Natural Earth's own `ISO_A3_EH` and `ISO_A2_EH` fields (`FRA` and `FR`, `NOR` and `NO`).
* Some features still have `-99` in both code fields. They are disputed or special areas that have no ISO 3166-1 code, for example Kosovo, Northern Cyprus, Somaliland, Siachen Glacier, Spratly Islands and Clipperton Island.
* A join on `ISO3166-1-Alpha-3` will not match those features. `-99` is also not a unique key: it appears on every one of them.
* Natural Earth draws country boundaries according to their de facto status (see its [disputed boundaries policy][ne-disputed]). They are not necessarily the borders that any one government claims.
* The outer rings of the polygons run clockwise. The build does not change ring direction. [RFC 7946][rfc7946] asks for counter-clockwise rings, but most tools accept both.
* Coordinates have at most 6 decimal places.

## Data sources

* [Natural Earth][naturalearth], 10m Admin-0 Countries ([download page][ne-admin0]): the polygons, the country name (its `admin` field) and the ISO codes (its `iso_a3`, `iso_a2`, `iso_a3_eh` and `iso_a2_eh` fields). Licence: public domain under its [terms of use][ne-terms].

Changes made to the source data: the 10m Admin-0 Countries file is converted to GeoJSON. Only the country name and the ISO 3166-1 alpha-2 and alpha-3 code fields are kept. For France and Norway, where Natural Earth has `-99` in its main code fields, the codes are taken from its `ISO_A2_EH` and `ISO_A3_EH` fields. Invalid geometries are repaired and coordinates are rounded to 6 decimal places.

Not endorsed by, or affiliated with, Natural Earth.

[naturalearth]: https://www.naturalearthdata.com/
[ne-admin0]: https://www.naturalearthdata.com/downloads/10m-cultural-vectors/10m-admin-0-countries/
[ne-terms]: https://www.naturalearthdata.com/about/terms-of-use/
[ne-disputed]: https://www.naturalearthdata.com/about/disputed-boundaries-policy/
[country-codes]: https://github.com/datasets/country-codes
[rfc7946]: https://datatracker.ietf.org/doc/html/rfc7946

## Preparation

The build needs `make`, `curl` and [GDAL][gdal] (for `ogr2ogr`). To check that GDAL is installed:

```bash
ogr2ogr --version
```

To rebuild `data/countries.geojson`:

```bash
make data
```

This downloads the latest 10m Admin-0 Countries file that Natural Earth publishes (the version is not pinned) into `ne_10m_admin_0_countries.zip`, converts it with `ogr2ogr` and saves the result in `data/countries.geojson`. The conversion keeps the three properties above, rounds coordinates to 6 decimal places and repairs invalid geometries (`-makevalid`, for example self-intersecting polygons). If the zip file is already there, it is reused. Run `make clean` to delete it.

A GitHub Actions workflow runs `make data` on the 1st of every month (and on pushes to `main` and on manual runs), and commits `data/countries.geojson` if it changed.

[gdal]: https://gdal.org/en/latest/download.html

## License

The geometry and the three properties come from [Natural Earth][naturalearth]. Its [terms of use][ne-terms] put the data in the public domain and allow commercial use without permission or credit. We found nothing in the file that Natural Earth credits to another provider: the three properties are Natural Earth's country name and ISO code fields.

The maintainers offer this package under the [Open Data Commons Public Domain Dedication and License][pddl] (PDDL) 1.0. A credit is not required, but a link back to [Natural Earth][naturalearth], [Lexman][lexman] and the [Open Knowledge Foundation][okfn] is appreciated. See [ATTRIBUTION.txt](ATTRIBUTION.txt).

All source code is licensed under the [MIT licence][mit].

[mit]: https://opensource.org/licenses/MIT
[pddl]: https://opendatacommons.org/licenses/pddl/1.0/
[lexman]: https://github.com/lexman
[okfn]: https://okfn.org/
