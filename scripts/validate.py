from util import root

from goodtables import validate
from goodtables.cli import _print_report

report = validate(
    str(root / "datapackage.json"),
    skip_checks=["unique-constraint"]
)
_print_report(report)
