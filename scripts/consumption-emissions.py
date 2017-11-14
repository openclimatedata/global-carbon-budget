import pandas as pd

from util import root, excel_national
from countrynames import to_code_3

consumption_emissions_csv = root / "data/consumption-emissions.csv"

# Consumption emissions
consumption_emissions = pd.read_excel(
    excel_national,
    sheet_name="Consumption Emissions GCB",
    skiprows=8,
    index_col=0
)
consumption_emissions.index.name = "Year"
consumption_emissions = consumption_emissions.T
consumption_emissions.index.rename("Name", inplace=True)

consumption_emissions["Code"] = [to_code_3(i) or i
                                 for i in consumption_emissions.index]

consumption_emissions = consumption_emissions.reset_index().drop(
    "Name", axis=1)

consumption_emissions = pd.melt(
    consumption_emissions,
    id_vars="Code",
    var_name="Year",
    value_name="Consumption-Emissions"
)

consumption_emissions.sort_values(["Code", "Year"], inplace=True)

consumption_emissions.dropna(inplace=True)

consumption_emissions.to_csv(
    consumption_emissions_csv,
    encoding="UTF-8",
    float_format="%.3f",
    index=False
)
