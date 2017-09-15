import numpy as np
import pandas as pd

from util import root, excel_national

emissions_transfers_csv = root / "data/emissions-transfers.csv"

# Emissions transfers
emissions_transfers = pd.read_excel(
    excel_national,
    sheetname="Emissions Transfers GCB",
    skiprows=7,
    index_col=0,
    header=[0, 1]
)
emissions_transfers.index.name = "Year"
emissions_transfers = emissions_transfers.T
emissions_transfers.index.rename(["CDIAC-Name", "Name"], inplace=True)

emissions_transfers = pd.melt(
    emissions_transfers.reset_index(),
    id_vars=['Name', 'CDIAC-Name'],
    var_name="Year",
    value_name="Emissions-Transfers"
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
with_data_and_in_range = (emissions_transfers.Name.isin(has_data) &
                          emissions_transfers.Year.isin(range(1990, 2015)))


emissions_transfers['Source'] = np.where(
    emissions_transfers.Year < 2012, "CDIAC", "BP")
emissions_transfers.ix[with_data_and_in_range, "Source"] = "UNFCCC"

emissions_transfers.dropna(inplace=True)

emissions_transfers.sort_values(["Name", "Year"], inplace=True)
emissions_transfers.to_csv(
    emissions_transfers_csv,
    encoding="UTF-8",
    float_format="%.3f",
    index=False
)
