The [Global Carbon Budget](https://globalcarbonbudget.org/) is an annual living data publication of carbon cycle
sources and sinks, generated from multiple data sources and by multiple
organisations and research groups.

This repository makes the data from the original Excel files available as CSVs.
Metadata and citation info is contained as comments at the beginning of the file with a `#` prefix.

In Python, they can be read with `pd.read_csv(filename, comment="#", index_col=0)`.

The data is generated using the [openclimatedata](github.com/openclimatedata/openclimatedata) library.
See also the [Openclimatedata website](https://openclimatedata.net/emissions/global-carbon-budget)

Maintainer of this repository is Robert Gieseke (<mail@openclimatedata.net>).
See below for [license information](#license).

## Data

- Global Carbon Budget

- Historical CO₂ budget

- Fossil emissions by category/fuel type

- Land-use change emissions

- Ocean CO₂ sink

- Terrestrial CO₂ sink

- Cement Carbonation sink (since 2020 version)

## Preparation

To update or regenerate the CSV files the following steps need to be run:

```
uv run scripts/generate.py
```

## License

The Global Carbon Budget Excel files contains:

> The use of data is conditional on citing the original data sources. Full details on how to cite the data are given at the top of each page. For research projects, if the data are essential to the work, or if an important result or conclusion depends on the data, co-authorship may need to be considered. The Global Carbon Project facilitates access to data to encourage its use and promote a good understanding of the carbon cycle. Respecting original data sources is key to help secure the support of data providers to enhance, maintain and update valuable data.

The files at the [ICOS data repository](https://www.icos-cp.eu/impact/science/global-carbon-budget) are released under a CC-BY license.

The source code in `scripts` is released under a
[CC0 Public Dedication License](https://creativecommons.org/publicdomain/zero/1.0/).
