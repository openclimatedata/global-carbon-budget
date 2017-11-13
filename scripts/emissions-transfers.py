import numpy as np
import pandas as pd

from util import root, excel_national

emissions_transfers_csv = root / "data/emissions-transfers.csv"

# Emissions transfers
emissions_transfers = pd.read_excel(
    excel_national,
    sheet_name="Emissions Transfers GCB",
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

emissions_transfers.dropna(inplace=True)

emissions_transfers.sort_values(["Name", "Year"], inplace=True)
emissions_transfers.to_csv(
    emissions_transfers_csv,
    encoding="UTF-8",
    float_format="%.3f",
    index=False
)
