# coding: utf-8

import os

import numpy as np
import pandas as pd

path = os.path.dirname(os.path.realpath(__file__))
excel_global = os.path.join(
    path,
    "../archive/Global_Carbon_Budget_2015_v1.1.xlsx"
)
excel_national = os.path.join(
    path,
    "../archive/National_Carbon_Emissions_2015_v1.1.xlsx"
)
fossil_fuel_csv = os.path.join(path, "../data/fossil-fuel-cement.csv")
land_use_csv = os.path.join(path, "../data/land-use-change.csv")
ocean_sink_csv = os.path.join(path, "../data/ocean-sink.csv")
terrestrial_sink_csv = os.path.join(path, "../data/terrestrial-sink.csv")
historical_budget_csv = os.path.join(path, "../data/historical-budget.csv")
territorial_cdiac_csv = os.path.join(
    path,
    "../data/territorial-emissions-cdiac.csv"
)
territorial_unfccc_csv = os.path.join(
    path,
    "../data/territorial-emissions-unfccc.csv"
)
consumption_emissions_csv = os.path.join(
    path,
    "../data/consumption-emissions.csv"
)
country_definitions_csv = os.path.join(
    path,
    "../data/country-definitions.csv"
)

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
    excel_global,
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
    excel_global,
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
    excel_global,
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
    excel_global,
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
    excel_global,
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


# Territorial CDIAC emissions

territorial_cdiac = pd.read_excel(
    excel_national,
    sheetname="Territorial Emissions CDIAC",
    skiprows=13,
    index_col=0,
    header=[0, 1]
)
territorial_cdiac.index.name = "Year"

territorial_cdiac = territorial_cdiac.T
territorial_cdiac.index.rename(["CDIAC-Name", "Name"], inplace=True)

territorial_cdiac = pd.melt(
    territorial_cdiac.reset_index(),
    id_vars=['Name', 'CDIAC-Name'],
    var_name="Year",
    value_name="Emissions"
)

territorial_cdiac['Source'] = np.where(
    territorial_cdiac.Year < 2012, "CDIAC", "BP")

# In 2012 to 2014 all data is based on BP.
assert((territorial_cdiac[territorial_cdiac.Year.isin(
    [2012, 2015])]["Source"] == "BP").all())

territorial_cdiac.sort_values(["Name", "Year"], inplace=True)

territorial_cdiac.to_csv(
    territorial_cdiac_csv,
    encoding="UTF-8",
    float_format="%.3f",
    index=False
)

# Territorial UNFCCC emissions

territorial_unfccc = pd.read_excel(
    excel_national,
    sheetname="Territorial Emissions UNFCCC",
    skiprows=13,
    index_col=0,
    header=[0, 1]
)
territorial_unfccc.index.name = "Year"

territorial_unfccc = territorial_unfccc.T
territorial_unfccc.index.rename(["CDIAC-Name", "Name"], inplace=True)

territorial_unfccc = pd.melt(
    territorial_unfccc.reset_index(),
    id_vars=['Name', 'CDIAC-Name'],
    var_name="Year",
    value_name="Emissions"
)

territorial_unfccc['Source'] = np.where(
    territorial_unfccc.Year < 2012, "CDIAC", "BP")

has_data = [
    'Australia', 'Austria', 'Belarus', 'Belgium', 'Bulgaria', 'Canada',
    'Croatia', 'Cyprus', 'Czech Republic', 'Denmark', 'Estonia', 'Finland',
    'France', 'Germany', 'Greece', 'Hungary', 'Iceland', 'Ireland', 'Italy',
    'Japan', 'Kazakhstan', 'Latvia', 'Liechtenstein', 'Lithuania',
    'Luxembourg', 'Malta', 'Netherlands', 'New Zealand', 'Norway', 'Poland',
    'Portugal', 'Romania', 'Russian Federation', 'Slovakia', 'Slovenia',
    'Spain', 'Sweden', 'Switzerland', 'Turkey', 'Ukraine', 'United Kingdom',
    'United States of America'
]
assert(len(has_data) == 42)
with_data_and_in_range = (territorial_unfccc.Name.isin(has_data) &
                          territorial_unfccc.Year.isin(range(1990, 2013)))
territorial_unfccc.ix[with_data_and_in_range, "Source"] = "UNFCCC"

# Check
# 42 countries have UNFCCC data available in 1990 - 2012
assert(territorial_unfccc[(territorial_unfccc.Source == "UNFCCC") &
                          territorial_unfccc.Name.isin(has_data) &
                          (territorial_unfccc.Year >= 1990) &
                          (territorial_unfccc.Year <  2013)
                          ]["Emissions"].count() == 42 * 23)
# In 2013 and 2014 all data is based on BP
assert((territorial_unfccc[territorial_unfccc.Year.isin(
    [2013, 2015])]["Source"] == "BP").all())

territorial_unfccc.sort_values(["Name", "Year"], inplace=True)

territorial_unfccc.to_csv(
    territorial_unfccc_csv,
    encoding="UTF-8",
    float_format="%.3f",
    index=False
)


# Consumption emissions
consumption_emissions = pd.read_excel(
    excel_national,
    sheetname="Consumption Emissions UNFCCC",
    skiprows=7,
    index_col=0,
    header=[0, 1]
)
consumption_emissions.index.name = "Year"
consumption_emissions = consumption_emissions.T
consumption_emissions.index.rename(["CDIAC-Name", "Name"], inplace=True)

consumption_emissions = pd.melt(
    consumption_emissions.reset_index(),
    id_vars=['Name', 'CDIAC-Name'],
    var_name="Year",
    value_name="Emissions"
)

consumption_emissions['Source'] = np.where(
    consumption_emissions.Year < 2012, "CDIAC", "BP")
consumption_emissions.ix[with_data_and_in_range, "Source"] = "UNFCCC"

consumption_emissions.dropna(inplace=True)

consumption_emissions.sort_values(["Name", "Year"], inplace=True)
consumption_emissions.to_csv(
    consumption_emissions_csv,
    encoding="UTF-8",
    float_format="%.3f",
    index=False
)

# Country Definitions
country_definitions = pd.read_excel(
    excel_national,
    sheetname="Country Definitions",
    skiprows=3
)

country_definitions.to_csv(
    country_definitions_csv,
    encoding="UTF-8",
    index=False
)
