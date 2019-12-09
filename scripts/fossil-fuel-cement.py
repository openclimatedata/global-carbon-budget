import pandas as pd

from util import root, excel_global

fossil_fuel_csv = root / "data/fossil-fuel-cement.csv"

# Fossil fuel and cement production emissions by fuel type
converters = {
    "Total": int,
    "Coal": int,
    "Oil": int,
    "Gas": int,
    "Cement": int,
    "Flaring": int
}

fossil_fuel_cement = pd.read_excel(
    excel_global,
    sheet_name="Fossil Emissions by Fuel Type",
    skiprows=12,
    index_col="Year",
    usecols="A:G",
    converters=converters
)

categories = ["Total", "Coal", "Oil", "Gas", "Cement", "Flaring"]
fossil_fuel_cement = pd.melt(
    fossil_fuel_cement.reset_index(),
    id_vars=["Year"],
    value_vars=categories,
    var_name="Category",
    value_name="Value"
)

fossil_fuel_cement.loc[fossil_fuel_cement.Year < 2017, "Source"] = "CDIAC"

fossil_fuel_cement.loc[fossil_fuel_cement.Year >= 2017, "Source"] = "BP"

fossil_fuel_cement.loc[
    (fossil_fuel_cement.Year >= 2017) &
    (fossil_fuel_cement.Category == "Cement"), "Source"
    ] = "US Geological Survey"

fossil_fuel_cement.loc[
    (fossil_fuel_cement.Year >= 2017) &
    (fossil_fuel_cement.Category == "Flaring"), "Source"] = "Constant"

fossil_fuel_cement.loc[
    (fossil_fuel_cement.Year >= 2017) &
    (fossil_fuel_cement.Category == "Total"), "Source"] = "Combination"

assert(len(fossil_fuel_cement[
    fossil_fuel_cement.Source == "US Geological Survey"] == 2))

assert(len(fossil_fuel_cement[
    fossil_fuel_cement.Source == "Constant"] == 2))

assert(len(fossil_fuel_cement[
    fossil_fuel_cement.Source == "Combination"] == 2))

fossil_fuel_cement.to_csv(fossil_fuel_csv, encoding="UTF-8", index=False)
