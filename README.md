The Global Carbon Budget is an annual living data publication of carbon cycle
sources and sinks, generated from multiple data sources and by multiple
organisations and research groups.

This [Data Package](http://frictionlessdata.io/specs/data-package/) makes the data from the 2017 Global Carbon Budget and National Emissions [Excel files](https://www.icos-cp.eu/GCP/2017) available as CSV files. For updates of the original data and further information refer to the
[Global Carbon Budget](http://www.globalcarbonproject.org/carbonbudget/index.htm) website.


## Data

### Global Carbon Budget

[Notes and Methods](doc/global-carbon-budget.md)

[global-carbon-budget](data/global-carbon-budget.csv)


### Fossil fuel and cement production emissions by fuel type

[Notes and Methods](doc/fossil-fuel-cement.md)

[fossil-fuel-cement.csv](data/fossil-fuel-cement.csv)

[fossil-fuel-cement-per-capita.csv](data/fossil-fuel-cement-per-capita.csv)


### Land-use change emissions

[Notes and Model References](doc/land-use-change.md)

[land-use-change.csv](data/land-use-change.csv)


### Ocean CO2 sink (positive values represent a flux from the atmosphere to the ocean)

[Notes and Model References](doc/ocean-sink.md)

[ocean-sink.csv](data/ocean-sink.csv)


### Terrestrial CO2 sink (positive values represent a flux from the atmosphere to the land)

[Notes and Model References](doc/terrestrial-sink.md)

[terrestrial-sink.csv](data/terrestrial-sink.csv)


### Historical CO2 budget

[Notes and References](doc/historical-budget.md)

[historical-budget.csv](data/historical-budget.csv)


### Territorial Emissions CDIAC

[Notes and Methods](doc/territorial-emissions-cdiac.md)

[territorial-emissions-cdiac.csv](data/territorial-emissions-cdiac.csv)


### Territorial Emissions GCB

[Notes and Methods](doc/territorial-emissions-gcb.md)

[territorial-emissions-unfccc.csv](data/territorial-emissions-gcb.csv)



### Consumption Emissions GCB

[Notes and Methods](doc/consumption-emissions.md)

[consumption-emissions.csv](data/consumption-emissions.csv)


### Emissions Transfers GCB

[Notes and Methods](doc/emissions-transfers.md)

[emissions-transfers.csv](data/emissions-transfers.csv)



### Country Definitions

Details of the geographical information corresponding to countries and regions used in this database for Consumption and Transfer emissions

[country-definitions.csv](data/country-definitions.csv)

## Preparation

To update or regenerate the CSV files the following steps need to be run:

Install requirements:

```
pip install -r scripts/requirements.txt
```

Run the script to generate CSV files:
```
python scripts/process.py
```


## Notes

A bug in the Ocean-Sink Excel sheet for the model average is fixed in this CSV.

The *Global Carbon Budget* data is written to CSV files using the
accuracy used for display in the original Excel, or one digit more files
assuming this to be the implied precision.

The *National Emissions* are written to CSV files with three significant digits
as this is the accuracy used for the CDIAC data in the Excel file, thus
rounding the numbers derived from splitting up countries or using trend data as
with BP emissions data.

If other accuracy is needed adjust the `process.py` script
accordingly.

## License

The Global Carbon Budget [data page](http://www.globalcarbonproject.org/carbonbudget/17/data.htm) states:

> The use of data is conditional on citing the original data sources. Full details on how to cite the data are given at the top of each page. For research projects, if the data are essential to the work, or if an important result or conclusion depends on the data, co-authorship may need to be considered. The Global Carbon Project facilitates access to data to encourage its use and promote a good understanding of the carbon cycle. Respecting original data sources is key to help secure the support of data providers to enhance, maintain and update valuable data.

The primary reference for the full Global Carbon Budget 2017 is:

Corinne Le Quéré, Robbie M. Andrew, Pierre Friedlingstein, Stephen Sitch, Julia Pongratz, Andrew C. Manning, Jan Ivar Korsbakken, Glen P. Peters, Josep G. Canadell, Robert B. Jackson, Thomas A. Boden, Pieter P. Tans, Oliver D. Andrews, Vivek Arora, Dorothee C. E. Bakker, Leticia Barbero, Meike Becker, Richard A. Betts, Laurent Bopp, Frédéric Chevallier, Louise P. Chini, Philippe Ciais, Cathy Cosca, Jessica Cross, Kim Currie, Thomas Gasser, Ian Harris, Judith Hauck, Vanessa Haverd, Richard A. Houghton, Christopher W. Hunt, George Hurtt, Tatiana Ilyina, Atul K. Jain, Etsushi Kato, Markus Kautz, Ralph F. Keeling, Kees Klein Goldewijk, Arne Körtzinger, Peter Landschützer, Nathalie Lefèvre, Andrew Lenton, Sebastian Lienert, Ivan Lima, Danica Lombardozzi, Nicolas Metzl, Frank Millero, Pedro M. S. Monteiro, David R. Munro, Julia E. M. S. Nabel, Shin-ichiro Nakaoka, Yukihiro Nojiri, X. Antoni Padin, Benjamin Pfeil, Denis Pierrot, Benjamin Poulter, Gregor Rehder, Janet Reimer, Christian Rödenbeck, Jörg Schwinger, Roland Séférian, Ingunn Skjelvan, Benjamin D. Stocker, Hanqin Tian, Bronte Tilbrook, Ingrid T. van der Laan-Luijkx, Guido R. van der Werf, Steven M. A. C. van Heuven, Nicolas Viovy, Nicolas Vuichard, Anthony P. Walker, Andrew J. Watson, Andrew J. Wiltshire, Sönke Zaehle, Dan Zhu: Global Carbon Budget 2017, Earth Syst. Sci. Data Discussions, 2017. <https://doi.org/10.5194/essd-2017-123>

Otherwise please refer as:

 Global Carbon Project (2017) Carbon budget and trends 2017. <http://www.globalcarbonproject.org/carbonbudget> published on 13 November 2017, along with any other original peer-reviewed papers and data sources as appropriate.

See also the [Global Carbon Budget Publications](http://www.globalcarbonproject.org/carbonbudget/17/publications.htm) page.

The source code in `scripts` and this data package itself are released under a
[CC0 Public Dedication License](https://creativecommons.org/publicdomain/zero/1.0/).
