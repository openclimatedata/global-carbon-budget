import pandas as pd

from util import root, excel_global

historical_budget_csv = root / "data/historical-budget.csv"

# Historical CO₂ budget

historical_budget = pd.read_excel(
    excel_global,
    sheet_name="Historical Budget",
    skiprows=14,
    index_col="Year",
    usecols="A:E"
)
historical_budget = historical_budget.rename(columns={
    "fossil fuel and industry": "Fossil-Fuel-Industry",
    "land-use change emissions": "Land-Use-Change",
    "atmospheric growth": "Atmospheric-Growth",
    "ocean sink": "Ocean-Sink"
})
historical_budget.to_csv(
    historical_budget_csv,
    encoding="UTF-8",
    float_format="%.3f"
)
