The Global Carbon Budget is an annual living data publication of carbon cycle
sources and sinks, generated from multiple data sources and by multiple
organisations and research groups.

This [Data Package](http://frictionlessdata.io/specs/data-package/) makes the data from the 2018 Global Carbon Budget and National Emissions [Excel files](https://www.icos-cp.eu/GCP/2018) v1.0 available as CSV files. For updates of the original data and further information refer to the
[Global Carbon Budget](http://www.globalcarbonproject.org/carbonbudget/index.htm) website.

Maintainer of this Data Package is Robert Gieseke (<robert.gieseke@pik-potsdam.de>).
See below for [license information](#license)

## Data

### Global Carbon Budget

[Notes and Methods](doc/global-carbon-budget.md)

[global-carbon-budget.csv](data/global-carbon-budget.csv)


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


### Territorial Emissions

[Notes and Methods](doc/territorial-emissions.md)

[territorial-emissions.csv](data/territorial-emissions.csv)


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

```
make clean
```

```
make
```

To validate the Data Package:
```
make validate
```


## Notes

The *Global Carbon Budget* data is written to CSV files using the
accuracy used for display in the original Excel, or one digit more files
assuming this to be the implied precision.

The *National Emissions* are written to CSV files with three significant digits
as this is the accuracy used for the CDIAC data in the Excel file, thus
rounding the numbers derived from splitting up countries or using trend data as
with BP emissions data.

If other accuracy is needed adjust the processing scripts accordingly.

## License

The Global Carbon Budget [data page](http://www.globalcarbonproject.org/carbonbudget/18/data.htm) states:

> The use of data is conditional on citing the original data sources. Full details on how to cite the data are given at the top of each page. For research projects, if the data are essential to the work, or if an important result or conclusion depends on the data, co-authorship may need to be considered. The Global Carbon Project facilitates access to data to encourage its use and promote a good understanding of the carbon cycle. Respecting original data sources is key to help secure the support of data providers to enhance, maintain and update valuable data.

The primary reference for the full Global Carbon Budget 2018 is:

Global Carbon Budget 2018, by Corinne Le Quéré, Robbie M. Andrew, Pierre Friedlingstein, Stephen Sitch, Judith Hauck, Julia Pongratz, Penelope A. Pickers, Jan Ivar Korsbakken, Glen P. Peters, Josep G. Canadell, Almut Arneth, Vivek K. Arora, Leticia Barbero, Ana Bastos, Laurent Bopp, Frédéric Chevallier, Louise P. Chini, Philippe Ciais, Scott C. Doney, Thanos Gkritzalis, Daniel S. Goll, Ian Harris, Vanessa Haverd, Forrest M. Hoffman, Mario Hoppema, Richard A. Houghton, George Hurtt, Tatiana Ilyina, Atul K. Jain, Truls Johannessen, Chris D. Jones, Etsushi Kato, Ralph F. Keeling, Kees Klein Goldewijk, Peter Landschützer, Nathalie Lefèvre, Sebastian Lienert, Zhu Liu, Danica Lombardozzi, Nicolas Metzl, David R. Munro, Julia E. M. S. Nabel, Shin-ichiro Nakaoka, Craig Neill, Are Olsen, Tsueno Ono, Prabir Patra, Anna Peregon, Wouter Peters, Philippe Peylin, Benjamin Pfeil, Denis Pierrot, Benjamin Poulter, Gregor Rehder, Laure Resplandy, Eddy Robertson, Matthias Rocher, Christian Rödenbeck, Ute Schuster, Jörg Schwinger, Roland Séférian, Ingunn Skjelvan, Tobias Steinhoff, Adrienne Sutton, Pieter P. Tans, Hanqin Tian, Bronte Tilbrook, Francesco N. Tubiello, Ingrid T. van der Laan-Luijkx, Guido R. van der Werf, Nicolas Viovy, Anthony P. Walker, Andrew J. Wiltshire, Rebecca Wright, Sönke Zaehle, and Bo Zheng (2018), Earth System Science Data, 10, 1-54, 2018, <https://doi.org/10.5194/essd-10-2141-2018>

Otherwise please refer as:

 Global Carbon Project (2018) Carbon budget and trends 2018. <www.globalcarbonproject.org/carbonbudget> published on 5 December 2018, along with any other original peer-reviewed papers and data sources as appropriate.

See also the [Global Carbon Budget Publications](http://www.globalcarbonproject.org/carbonbudget/17/publications.htm) page.

The source code in `scripts` and the metadata in this Data Package itself are released under a
[CC0 Public Dedication License](https://creativecommons.org/publicdomain/zero/1.0/).
