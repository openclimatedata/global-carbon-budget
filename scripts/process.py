# coding: utf-8

import os

import numpy as np
import pandas as pd

path = os.path.dirname(os.path.realpath(__file__))
excel_file = os.path.join(path,
                          "../archive/Global_Carbon_Budget_2015_v1.1.xlsx")

fossil_fuel_csv = os.path.join(path, "../data/fossil-fuel-cement.csv")
land_use_csv = os.path.join(path, "../data/land-use-change.csv")
ocean_sink_csv = os.path.join(path, "../data/ocean-sink.csv")
terrestrial_sink_csv = os.path.join(path, "../data/terrestrial-sink.csv")
historical_budget_csv = os.path.join(path, "../data/historical-budget.csv")


# Fossil fuel and cement production emissions by fuel type
converters = {
    "Total": int,
    "Coal": int,
    "Oil": int,
    "Gas": int,
    "Cement": int,
    "Flaring": int,
    "Per Capita": lambda x: round(x, 2)
}
fossil_fuel_cement = pd.read_excel(
    excel_file,
    sheetname="Fossil Emissions by Fuel Type",
    skiprows=10,
    index_col="Year",
    parse_cols="A:H",
    converters=converters
)
fossil_fuel_cement['Source'] = np.where(
    fossil_fuel_cement.index < 2012, 'CDIAC', 'BP')
fossil_fuel_cement.to_csv(fossil_fuel_csv, encoding="UTF-8")


# Land-use change emissions
landuse_change = pd.read_excel(
    excel_file,
    sheetname="Land-Use Change Emissions",
    skiprows=21,
    index_col="Year",
    parse_cols="A:B,D,E,G:P,R"
)
column_names = {
    "in the global carbon budget": "Land-Use-Change",
    "Ensemble": "Mean-Model-Ensemble"
}
column_names[landuse_change.columns[2]] = "GFED4.1"
landuse_change = landuse_change.rename(columns=column_names)
landuse_change.columns = [c.strip() for c in landuse_change.columns]
landuse_change.head()

landuse_change.to_csv(
    land_use_csv,
    float_format="%.3f",
    encoding="UTF-8"

)


# Ocean CO2 sink

ocean_sink = pd.read_excel(
    excel_file,
    sheetname="Ocean Sink",
    skiprows=25,
    skip_footer=2,
    index_col="year",
    parse_cols="A:B,D:K,M:N"
)
ocean_sink.index.name = "Year"
ocean_sink = ocean_sink.rename(columns={
    "and models used in the global carbon budget": "Ocean-Sink"
    })
ocean_sink.columns = [c.replace(" ", "") for c in ocean_sink.columns]
ocean_sink.to_csv(
    ocean_sink_csv,
    encoding="UTF-8",
    float_format="%.2f"
)


# Terrestrial CO₂ sink

terrestrial_sink = pd.read_excel(
    excel_file,
    sheetname="Terrestrial Sink",
    skiprows=17,
    index_col="Year",
    parse_cols="A:B,D:M,O"
)
terrestrial_sink = terrestrial_sink.rename(columns={
    " of the global carbon budget": "Terrestrial-Sink"
})
terrestrial_sink.columns = [c.strip() for c in terrestrial_sink.columns]

terrestrial_sink.insert(
    1,
    'Preliminary',
    np.where(terrestrial_sink.index < 1997, 'false', 'true')
)
terrestrial_sink.to_csv(
    terrestrial_sink_csv,
    encoding="UTF-8",
    float_format="%.3f"
)


# Historical CO₂ budget

historical_budget = pd.read_excel(
    excel_file,
    sheetname="Historical Budget",
    skiprows=14,
    index_col="Year",
    parse_cols="A:E"
)
historical_budget = historical_budget.rename(columns={
    "fossil fuel and cement emissions": "Fossil-Fuel-Cement",
    "land-use change emissions": "Land-Use-Change",
    "atmospheric growth": "Atmospheric-Growth",
    "ocean sink": "Ocean-Sink"
})
historical_budget.to_csv(
    historical_budget_csv,
    encoding="UTF-8",
    float_format="%.3f"
)
