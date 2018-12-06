import pandas as pd

from util import root, excel_national
from countrynames import to_code_3

emissions_transfers_csv = root / "data/emissions-transfers.csv"

# Emissions transfers
emissions_transfers = pd.read_excel(
    excel_national,
    sheet_name="Emissions Transfers",
    skiprows=8,
    index_col=0
)
emissions_transfers.index.name = "Year"
emissions_transfers = emissions_transfers.T
emissions_transfers.index.rename("Name", inplace=True)

emissions_transfers["Code"] = [to_code_3(i) or i
                               for i in emissions_transfers.index]

emissions_transfers = emissions_transfers.reset_index().drop(
    "Name", axis=1)


emissions_transfers = pd.melt(
    emissions_transfers,
    id_vars="Code",
    var_name="Year",
    value_name="Emissions-Transfers"
)

emissions_transfers.sort_values(["Code", "Year"], inplace=True)
emissions_transfers.dropna(inplace=True)

emissions_transfers.to_csv(
    emissions_transfers_csv,
    encoding="UTF-8",
    float_format="%.3f",
    index=False
)
