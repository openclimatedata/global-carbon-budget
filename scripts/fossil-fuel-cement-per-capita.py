import pandas as pd

from util import root, excel_global

fossil_fuel_per_capita = root / "data/fossil-fuel-cement-per-capita.csv"

# Fossil fuel and cement production emissions by fuel type
converters = {
    "Per Capita": lambda x: round(x, 2)
}

fossil_fuel_cement = pd.read_excel(
    excel_global,
    sheet_name="Fossil Emissions by Fuel Type",
    skiprows=12,
    index_col="Year",
    usecols="A,H",
    converters=converters
)

fossil_fuel_cement.loc[fossil_fuel_cement.index < 2017, "Source"] = "CDIAC"

fossil_fuel_cement.loc[fossil_fuel_cement.index >= 2018, "Source"] = "BP"

fossil_fuel_cement.to_csv(fossil_fuel_per_capita, encoding="UTF-8")
