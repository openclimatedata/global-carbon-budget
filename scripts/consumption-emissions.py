import numpy as np
import pandas as pd

from util import root, excel_national


consumption_emissions_csv = root / "data/consumption-emissions.csv"

# Consumption emissions
consumption_emissions = pd.read_excel(
    excel_national,
    sheet_name="Consumption Emissions GCB",
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

consumption_emissions.dropna(inplace=True)

consumption_emissions.sort_values(["Name", "Year"], inplace=True)
consumption_emissions.to_csv(
    consumption_emissions_csv,
    encoding="UTF-8",
    float_format="%.3f",
    index=False
)
