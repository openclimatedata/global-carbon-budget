import pandas as pd

from util import root, excel_global

land_use_csv = root / "data/land-use-change.csv"

# Land-use change emissions
landuse_change = pd.read_excel(
    excel_global,
    sheetname="Land-Use Change Emissions",
    skiprows=16,
    index_col="Year",
    parse_cols="A:B,D,E,G:K"
)
column_names = {
    "in the global carbon budget": "Land-Use-Change"
}
column_names[landuse_change.columns[2]] = "GFED4.1"
landuse_change = landuse_change.rename(columns=column_names)
landuse_change.columns = [c.strip() for c in landuse_change.columns]
landuse_change.head()

landuse_change.to_csv(
    land_use_csv,
    float_format="%.3f",
    encoding="UTF-8"

)
