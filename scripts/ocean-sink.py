import pandas as pd

from util import root, excel_global

ocean_sink_csv = root / "data/ocean-sink.csv"

# Ocean CO2 sink

ocean_sink = pd.read_excel(
    excel_global,
    sheet_name="Ocean Sink",
    skiprows=19,
    skipfooter=1,
    index_col="year",
    usecols="A:B,D:J,L:M"
)
ocean_sink.index.name = "Year"

ocean_sink.rename(columns={"GCB": "Ocean-Sink"}, inplace=True)

ocean_sink.to_csv(
    ocean_sink_csv,
    encoding="UTF-8",
    float_format="%.3f"
)
