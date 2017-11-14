import numpy as np
import pandas as pd

from util import root, excel_national
from countrynames import to_code_3


territorial_cdiac_csv = root / "data/territorial-emissions-cdiac.csv"

# Territorial CDIAC emissions

territorial_cdiac = pd.read_excel(
    excel_national,
    sheet_name="Territorial Emissions CDIAC",
    skiprows=13,
    index_col=0
)
territorial_cdiac.index.name = "Year"

territorial_cdiac = territorial_cdiac.T
territorial_cdiac.index.rename("Name", inplace=True)

territorial_cdiac["Code"] = [to_code_3(i) or i
                             for i in territorial_cdiac.index]

territorial_cdiac = territorial_cdiac.reset_index().drop("Name", axis=1)

territorial_cdiac = pd.melt(
    territorial_cdiac,
    id_vars="Code",
    var_name="Year",
    value_name="Emissions"
)

territorial_cdiac.dropna(inplace=True)

territorial_cdiac.sort_values(["Code", "Year"], inplace=True)

territorial_cdiac.to_csv(
    territorial_cdiac_csv,
    encoding="UTF-8",
    float_format="%.3f",
    index=False
)
