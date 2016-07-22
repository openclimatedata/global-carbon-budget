The Global Carbon Budget is an annual living data publication of carbon cycle
sources and sinks, generated from multiple data sources and by multiple
organisations and research groups.

This data package makes the data from the 2015 Global Carbon Budget and National Emissions [Excel files](http://cdiac.ornl.gov/GCP/) available as CSV files. For updates of the original data and further information refer to the
[Global Carbon Budget](http://www.globalcarbonproject.org/carbonbudget/index.htm) website.


## Data

### Fossil fuel and cement production emissions by fuel type

[Notes and Methods](doc/fossil-fuel-cement.md)

[fossil-fuel-cement.csv](data/fossil-fuel-cement.csv)


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


### Territorial Emissions UNFCCC

[Notes and Methods](doc/territorial-emissions-unfccc.md)

[territorial-emissions-unfccc.csv](data/territorial-emissions-unfccc.csv)



### Consumption Emissions UNFCCC
...


### Emissions Transfers UNFCCC
...


### Country Definitions

...

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

For the *Global Carbon Budget* data is written to the CSV files using the
accuracy used for display in the original Excel files assuming this to be the
implied precision.

The *National Emissions* are written to CSV files with three significant digits
as this is the accuracy used for the CDIAC data in the Excel file, thus
rounding the numbers derived from splitting up countries or using trend data as
with BP emissions data.

If other accuracy is needed adjust the `process.py` script
accordingly.

## License

The Global Carbon Budget [data page](http://www.globalcarbonproject.org/carbonbudget/15/data.htm) states:

> The use of data is conditional on citing the original data sources. Full details on how to cite the data are given at the top of each page. For research projects, if the data are essential to the work, or if an important result or conclusion depends on the data, co-authorship may need to be considered. The Global Carbon Project facilitates access to data to encourage its use and promote a good understanding of the carbon cycle. Respecting original data sources is key to help secure the support of data providers to enhance, maintain and update valuable data.

The primary reference for Carbon Budget 2015 is:

Global Carbon Budget 2015, by C Le Quéré, R Moriarty, RM Andrew, JG Canadell, S Sitch, JI Korsbakken, P Friedlingstein, GP Peters, RJ Andres, TA Boden, RA Houghton, JI House, RF Keeling, P Tans, A Arneth, DCE Bakker, L Barbero , L Bopp, J Chang, F Chevallier, LP Chini, P Ciais, M Fader, R Feely, T Gkritzalis, I Harris, J Hauck, T Ilyina, AK Jain, E Kato, V Kitidis, K Klein Goldewijk, C Koven, P Landschützer, SK Lauvset, N Lefèvre, A Lenton, ID Lima, N Metzl, F Millero, DR Munro, A Murata, JEMS Nabel, S Nakaoka, Y Nojiri, K O'Brien, A Olsen, T Ono, FF Pérez, B Pfeil, D Pierrot, B Poulter, G Rehder, C Rödenbeck, S Saito, U Schuster, J Schwinger, R Séférian, T Steinhoff, BD Stocker, AJ Sutton, T Takahashi, B Tilbrook, IT van der Laan-Luijkx, GR van der Werf, S van Heuven, D Vandemark, N Viovy, A Wiltshire, S Zaehle, and N Zeng (2015), Earth System Science Data, DOI:[10.5194/essd-7-349-2015](https://doi.org/10.5194/essd-7-349-2015).

Otherwise please refer as:

Global Carbon Project (2015) Carbon budget and trends 2015. <www.globalcarbonproject.org/carbonbudget> published on 7 December 2015, along with any other original peer-reviewed papers and data sources as appropriate.

See also the [Global Carbon Budget Publications](http://www.globalcarbonproject.org/carbonbudget/15/publications.htm) page.

The source code in `scripts` and this data package itself are released under a
[CC0 Public Dedication License](https://creativecommons.org/publicdomain/zero/1.0/).
