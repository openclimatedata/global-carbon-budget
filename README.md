> The Global Carbon Project was formed to assist the international science
> community to establish a common, mutually agreed knowledge base supporting
> policy debate and action to slow the rate of increase of greenhouse gases in
> the atmosphere.

[…]

> The scientific goal of the Global Carbon Project is to develop a complete
> picture of the global carbon cycle, including both its biophysical and human
> dimensions together with the interactions and feedbacks between them.

(<http://www.globalcarbonproject.org/about/index.htm>)

This data package makes the data from the 2015 Global Carbon Budget and National Emissions [Excel files](http://cdiac.ornl.gov/GCP/) available as CSV files.


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

Run the script to generate
```
python scripts/process.py
```


## Notes

Data is written to the CSV files using the accuracy used for display in the
original Excel files.


## License

The Global Carbon Budget [data page] states:

> The use of data is conditional on citing the original data sources. Full details on how to cite the data are given at the top of each page. For research projects, if the data are essential to the work, or if an important result or conclusion depends on the data, co-authorship may need to be considered. The Global Carbon Project facilitates access to data to encourage its use and promote a good understanding of the carbon cycle. Respecting original data sources is key to help secure the support of data providers to enhance, maintain and update valuable data.

The source code in `scripts` and this data package itself are released under a
[CC0 Public Dedication License](https://creativecommons.org/publicdomain/zero/1.0/).
