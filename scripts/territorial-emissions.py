import numpy as np
import pandas as pd

from util import root, excel_national
from countrynames import to_code_3
from countrygroups import ANNEX_ONE_KAZ as annex_one

territorial_gcb_csv = root / "data/territorial-emissions.csv"

# Territorial GCB emissions

territorial_gcb = pd.read_excel(
    excel_national,
    sheet_name="Territorial Emissions",
    skiprows=16,
    index_col=0,
    usecols="A:HV"
)
territorial_gcb.index.name = "Year"

territorial_gcb = territorial_gcb.T
territorial_gcb.index.rename("Name", inplace=True)

territorial_gcb["Code"] = [to_code_3(i) or i for i in territorial_gcb.index]

territorial_gcb = territorial_gcb.reset_index().drop("Name", axis=1)

territorial_gcb = pd.melt(
    territorial_gcb,
    id_vars='Code',
    var_name="Year",
    value_name="Emissions"
)

territorial_gcb.sort_values(["Code", "Year"], inplace=True)

territorial_gcb['Source'] = np.where(
    territorial_gcb.Year < 2015, "CDIAC", "BP")


# The Global Carbon Budget doesn't list EU as having source UNFCCC and Monaco
# is included with France (as in CDIAC)
annex_one.remove("EUU")
annex_one.remove("MCO")
assert(len(annex_one) == 42)

with_data_and_in_range = (territorial_gcb.Code.isin(annex_one) &
                          territorial_gcb.Year.isin(range(1990, 2017)))
territorial_gcb.loc[with_data_and_in_range, "Source"] = "UNFCCC"

# Check
# 42 countries have UNFCCC data given as source in 1990 - 2016
assert(territorial_gcb[
    (territorial_gcb.Source == "UNFCCC") &
    territorial_gcb.Code.isin(annex_one) &
    (territorial_gcb.Year >= 1990) &
    (territorial_gcb.Year <= 2016)]["Emissions"].count() == len(annex_one) * 27)

# In 2017 all data is based on BP
assert((territorial_gcb[territorial_gcb.Year.isin(
    [2017])]["Source"] == "BP").all())
# Total BP count should be 2015 plus 2016 plus 2017.
count = len(territorial_gcb.Code.unique())
assert(
    len(territorial_gcb.loc[territorial_gcb.Source == 'BP']) ==
    3 * count - 2 * len(annex_one)
)

territorial_gcb.to_csv(
    territorial_gcb_csv,
    encoding="UTF-8",
    float_format="%.3f",
    index=False
)
