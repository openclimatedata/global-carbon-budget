import pandas as pd

from util import root, excel_national


country_definitions_csv = root / "data/country-definitions.csv"

# Country Definitions
country_definitions = pd.read_excel(
    excel_national,
    sheet_name="Country Definitions",
    skiprows=3
)

country_definitions.to_csv(
    country_definitions_csv,
    encoding="UTF-8",
    index=False
)
