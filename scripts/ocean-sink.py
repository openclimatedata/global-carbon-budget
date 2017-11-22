import pandas as pd

from util import root, excel_global

ocean_sink_csv = root / "data/ocean-sink.csv"

# Ocean CO2 sink

ocean_sink = pd.read_excel(
    excel_global,
    sheet_name="Ocean Sink",
    skiprows=20,
    skipfooter=1,
    index_col="year",
    usecols="A:B,D:K,M:N"
)
ocean_sink.index.name = "Year"

ocean_sink.rename(columns={"GCB": "Ocean-Sink"}, inplace=True)

# Fix the GCB column, as the last column was not included in the original Excel
# calculation in v1.1 (#1).
ocean_sink["Ocean-Sink"] = ocean_sink.loc[:, "CCSM-BEC":"NorESM-OC"].mean(
    axis=1)

ocean_sink.to_csv(
    ocean_sink_csv,
    encoding="UTF-8",
    float_format="%.3f"
)
