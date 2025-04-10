<a className="gh-badge" href="https://datahub.io/core/geo-countries"><img src="https://badgen.net/badge/icon/View%20on%20datahub.io/orange?icon=https://datahub.io/datahub-cube-badge-icon.svg&label&scale=1.25" alt="badge" /></a>

## Description

Geodata [data package][datapackage] providing geojson polygons for all the world's countries.
Perfect for use in apps and visualizations.

## Data

The data comes from [Natural Earth][naturalearth], a community effort to make visually pleasing, well-crafted maps with cartography or GIS software at small scale.

More info about countries can be obtained from datapackage https://github.com/datasets/country-codes by a join on field ISO3166-1-Alpha-3

[naturalearth]: https://www.naturalearthdata.com/
[datapackage]: https://datapackage.org/standard/data-package/

## Preparation

To run the script and update the data:

### Prerequisites

1. Install required tools:
   - [GDAL](https://gdal.org/en/latest/download.html) - for geographic data processing

2. Verify GDAL installation:
   ```bash
   ogr2ogr --version
   ```

### Data Processing

The project uses `ogr2ogr` to convert Natural Earth's country boundaries from Shapefile to GeoJSON format, with the following features:
- Coordinate precision set to 6 decimal places
- Geometry validation enabled (`-makevalid`):
  - Fixes self-intersecting polygons
  - Corrects ring orientation
  - Removes duplicate vertices
  - Ensures geometric validity for better compatibility with GIS tools
- Selected fields:
  - `name`: Common name of the country (from admin field)
  - `ISO3166-1-Alpha-2`: Two-letter ISO country code (from iso_a2 field)
  - `ISO3166-1-Alpha-3`: Three-letter ISO country code (from iso_a3 field)

To process the data:
  ```bash
  make data
  ```

This will:
1. Download the Natural Earth countries dataset
2. Convert it to GeoJSON format with the specified settings
3. Save the result in `data/countries.geojson`

## License

All data is licensed under the [Open Data Commons Public Domain Dedication and License][pddl]. 

Note that the original data from [Natural Earth][naturalearth] is public domain. While no credit is 
formally required a link back or credit to [Natural Earth][naturalearth], [Lexman][lexman] and the [Open Knowledge Foundation][okfn] is much appreciated.

All source code is licenced under the [MIT licence][mit].

[mit]: https://opensource.org/licenses/MIT
[naturalearth]: https://www.naturalearthdata.com/
[pddl]: https://opendatacommons.org/licenses/pddl/1.0/
[lexman]: https://github.com/lexman
[okfn]: https://okfn.org/