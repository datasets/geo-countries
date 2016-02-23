Geodata [data package][datapackage] providing geojson polygons for all the world's countries.
Perfect for use in apps and visualizations.

## Data

The data comes from [Natural Earth][naturalearth], a community effort to make visually pleasing, well-crafted maps with cartography or GIS software at small scale.

The shape of the countries have two fields : 
* name : the common name for the country
* ISO3166-1-Alpha-3 : three letters iso code of the country

More info about countries can be get from datapackage https://github.com/datasets/country-codes by a join on field ISO3166-1-Alpha-3

[naturalearth]: http://www.naturalearthdata.com/
[datapackage]: http://dataprotocols.org/data-packages/

## Preparation

To run the script in order to update the data : see [scripts README](scripts/README.md)

## License

All data is licensed under the [Open Data Commons Public Domain Dedication and License][pddl]. 

Note that the original data from [Natural Earth][naturalearth] is public domain. While no credit is 
formally required a link back or credit to [Natural Earth][naturalearth], [Lexman][lexman] and the [Open Knowledge Foundation][okfn] is much appreciated.

All source code is licenced under the [MIT licence][mit].

[mit]: https://opensource.org/licenses/MIT
[naturalearth]: http://www.naturalearthdata.com/
[pddl]: http://opendatacommons.org/licenses/pddl/1.0/
[lexman]: http://github.com/lexman
[okfn]: http://okfn.org/





