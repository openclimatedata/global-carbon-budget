import numpy as np
import pandas as pd

from util import root, excel_global

terrestrial_sink_csv = root / "data/terrestrial-sink.csv"

# Terrestrial CO₂ sink

terrestrial_sink = pd.read_excel(
    excel_global,
    sheetname="Terrestrial Sink",
    skiprows=21,
    index_col="Year",
    parse_cols="A:B,D:Q"
)
terrestrial_sink = terrestrial_sink.rename(columns={
    " of the global carbon budget": "Terrestrial-Sink"
})
terrestrial_sink.columns = [c.strip() for c in terrestrial_sink.columns]

terrestrial_sink.insert(
    1,
    'Preliminary',
    np.where(terrestrial_sink.index < 1997, 'false', 'true')
)
terrestrial_sink.to_csv(
    terrestrial_sink_csv,
    encoding="UTF-8",
    float_format="%.3f"
)
