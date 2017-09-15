import numpy as np
import pandas as pd

from util import root, excel_national


territorial_gcb_csv = root / "data/territorial-emissions-gcb.csv"

# Territorial GCB emissions

territorial_gcb = pd.read_excel(
    excel_national,
    sheetname="Territorial Emissions GCB",
    skiprows=14,
    index_col=0,
    parse_cols="A:IB",
    header=[0, 1]
)
territorial_gcb.index.name = "Year"

territorial_gcb = territorial_gcb.T
territorial_gcb.index.rename(["CDIAC-Name", "Name"], inplace=True)

territorial_gcb = pd.melt(
    territorial_gcb.reset_index(),
    id_vars=['Name', 'CDIAC-Name'],
    var_name="Year",
    value_name="Emissions"
)

territorial_gcb['Source'] = np.where(
    territorial_gcb.Year < 2014, "CDIAC", "BP")
territorial_gcb.loc[
    (territorial_gcb.Name == "China") &
    (territorial_gcb.Year.isin(range(1990, 2016))),
    "Source"] = "BP"
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
with_data_and_in_range = (territorial_gcb.Name.isin(has_data) &
                          territorial_gcb.Year.isin(range(1990, 2015)))
territorial_gcb.ix[with_data_and_in_range, "Source"] = "UNFCCC"

# Check
# 42 countries have UNFCCC data available in 1990 - 2014
assert(territorial_gcb[
    (territorial_gcb.Source == "UNFCCC") &
    territorial_gcb.Name.isin(has_data) &
    (territorial_gcb.Year >= 1990) &
    (territorial_gcb.Year < 2015)]["Emissions"].count() == 42 * 25)

# In 2015 all data is based on BP
assert((territorial_gcb[territorial_gcb.Year.isin(
    [2015])]["Source"] == "BP").all())
# Total BP count should be 2014 plus 2015 plus China from 1990.
count = len(territorial_gcb.Name.unique())
assert(
    len(territorial_gcb.loc[territorial_gcb.Source == 'BP']) ==
    count + count - len(has_data) + len(range(1990, 2014))
)

territorial_gcb.sort_values(["Name", "Year"], inplace=True)

territorial_gcb.to_csv(
    territorial_gcb_csv,
    encoding="UTF-8",
    float_format="%.3f",
    index=False
)
