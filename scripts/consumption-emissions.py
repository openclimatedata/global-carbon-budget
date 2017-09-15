import numpy as np
import pandas as pd

from util import root, excel_national


consumption_emissions_csv = root / "data/consumption-emissions.csv"

# Consumption emissions
consumption_emissions = pd.read_excel(
    excel_national,
    sheetname="Consumption Emissions GCB",
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
    value_name="Consumption-Emissions"
)

has_data = [
    'Australia', 'Austria', 'Belarus', 'Belgium', 'Bulgaria', 'Canada',
    'Croatia', 'Cyprus', 'Czech Republic', 'Denmark', 'Estonia', 'Finland',
    'France', 'Germany', 'Greece', 'Hungary', 'Iceland', 'Ireland', 'Italy',
    'Japan', 'Kazakhstan', 'Latvia', 'Liechtenstein', 'Lithuania',
    'Luxembourg', 'Malta', 'Netherlands', 'New Zealand', 'Norway', 'Poland',
    'Portugal', 'Romania', 'Russian Federation', 'Slovakia', 'Slovenia',
    'Spain', 'Sweden', 'Switzerland', 'Turkey', 'Ukraine', 'United Kingdom',
    'USA'
]
assert(len(has_data) == 42)
with_data_and_in_range = (consumption_emissions.Name.isin(has_data) &
                          consumption_emissions.Year.isin(range(1990, 2015)))

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
