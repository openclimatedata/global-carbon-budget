import numpy as np
import pandas as pd

from util import root, excel_national

territorial_cdiac_csv = root / "data/territorial-emissions-cdiac.csv"

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
