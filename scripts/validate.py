from util import root

from goodtables import validate
from goodtables.cli import _print_report

report = validate(
    str(root / "datapackage.json"),
    table_limit=20,
    row_limit=20000
)
_print_report(report)
