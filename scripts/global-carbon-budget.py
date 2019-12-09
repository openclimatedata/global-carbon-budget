import pandas as pd

from util import root, excel_global

gcb_csv = root / "data/global-carbon-budget.csv"

# Global Carbon Budget

gcb = pd.read_excel(
    excel_global,
    sheet_name="Global Carbon Budget",
    skiprows=18,
    index_col="Year",
    usecols="B:H"
)

gcb.columns = [i.title().replace(" ", "-") for i in gcb.columns]

gcb.to_csv(
    gcb_csv,
    encoding="UTF-8",
    float_format="%.3f"
)
