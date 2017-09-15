import pandas as pd

from util import root, excel_global

ocean_sink_csv = root / "data/ocean-sink.csv"

# Ocean CO2 sink

ocean_sink = pd.read_excel(
    excel_global,
    sheetname="Ocean Sink",
    skiprows=24,
    skip_footer=2,
    index_col="year",
    parse_cols="A:B,D:J,L:M"
)
ocean_sink.index.name = "Year"
ocean_sink = ocean_sink.rename(columns={
    "and models used in the global carbon budget": "Ocean-Sink"
    })
ocean_sink.columns = [c.replace(" ", "") for c in ocean_sink.columns]
ocean_sink.to_csv(
    ocean_sink_csv,
    encoding="UTF-8",
    float_format="%.2f"
)
