from pandas_datapackage_reader import read_datapackage
from util import root

from pandas.testing import assert_series_equal

dp = read_datapackage(root)


ffi = dp["fossil-fuel-cement"].drop(
    "Source", axis=1).unstack("Category")
ffi.columns = ffi.columns.droplevel()

assert_series_equal(
    dp["global-carbon-budget"]["Fossil-Fuel-And-Industry"],
    ffi["Total"].astype(int) / 1000,  # convert to GtC
    check_exact=False,
    check_less_precise=True,
    check_names=False
)

assert_series_equal(
    dp["global-carbon-budget"]["Land-Use-Change-Emissions"],
    dp["land-use-change"]["Land-Use-Change"],
    check_exact=False,
    check_less_precise=True,
    check_names=False
)

assert_series_equal(
    dp["global-carbon-budget"]["Ocean-Sink"],
    dp["ocean-sink"]["Ocean-Sink"]
)

print("Comparison in 'checks.py' ok.")
