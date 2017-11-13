import numpy as np
import pandas as pd

from util import root, excel_national

territorial_cdiac_csv = root / "data/territorial-emissions-cdiac.csv"

# Territorial CDIAC emissions

territorial_cdiac = pd.read_excel(
    excel_national,
    sheet_name="Territorial Emissions CDIAC",
    skiprows=12,
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

territorial_cdiac.dropna(inplace=True)

territorial_cdiac.sort_values(["Name", "Year"], inplace=True)

territorial_cdiac.to_csv(
    territorial_cdiac_csv,
    encoding="UTF-8",
    float_format="%.3f",
    index=False
)
