# /// script
# requires-python = ">=3.14"
# dependencies = [
#     "openclimatedata==0.38.1",
# ]
# ///

from pathlib import Path

import openclimatedata as ocd

root = Path(__file__).parents[1]


print(f"openclimatedata, version {ocd.__version__}")

global_budget_single_tables = [
    {"sheet_name": "Global Carbon Budget", "slug": "global-carbon-budget"},
    {"sheet_name": "Historical Budget", "slug": "historical-budget"},
    {"sheet_name": "Fossil Emissions", "slug": "fossil-emissions"},
    {"sheet_name": "Cement Carbonation Sink", "slug": "cement-carbonation-sink"},
]

global_budget_with_subtables = [
    {"sheet_name": "Land-Use Change Emissions", "slug": "land-use-change-emissions"},
    {"sheet_name": "Ocean Sink", "slug": "ocean-sink"},
    {"sheet_name": "Terrestrial Sink", "slug": "terrestrial-sink"},
    {"sheet_name": "Atmospheric Growth", "slug": "atmospheric-growth"},
]


def comment_notes(notes, filename):
    commented_notes = "\n".join([f"# {line}".strip() for line in notes.split("\n")])
    commented_notes += f"\n# Generated with openclimatedata {ocd.__version__} from the GCB Excel file '{filename}' from https://doi.org/{ocd.Global_Carbon_Budget[version].doi}"
    commented_notes += "\n# http://openclimatedata.net - https://github.com/openclimatedata/global-carbon-budget"
    commented_notes += "\n"
    return commented_notes


for version in ocd.Global_Carbon_Budget.keys():
    print(f"Release Global Carbon Budget {version}")

    for item in global_budget_single_tables:
        sheet_name = item["sheet_name"]
        slug = item["slug"]
        if (slug == "cement-carbonation-sink") and (int(version) <= 2019):
            continue

        if slug == "fossil-emissions":
            if int(version) <= 2019:
                sheet_name += " by Fuel Type"
            else:
                sheet_name += " by Category"

        print(f"Sheet: {sheet_name}")

        notes = ocd.Global_Carbon_Budget[version].Global_Budget[sheet_name].__repr__()
        commented_notes = comment_notes(notes, ocd.Global_Carbon_Budget[version].Global_Budget.filename)
        csv_data = ocd.Global_Carbon_Budget[version].Global_Budget[sheet_name].to_dataframe().to_csv()

        filepath = f"data/global-carbon-budget-{version}-{slug}.csv"
        print(filepath)

        with open(root / filepath, "w") as f:
            f.write(commented_notes)
            f.write(csv_data)

    for item in global_budget_with_subtables:
        sheet_name = item["sheet_name"]
        slug = item["slug"]

        print(f"Sheet: {sheet_name}")

        if sheet_name not in ocd.Global_Carbon_Budget[version].Global_Budget:
            continue
        notes = ocd.Global_Carbon_Budget[version].Global_Budget[sheet_name].__repr__()
        commented_notes = comment_notes(notes, ocd.Global_Carbon_Budget[version].Global_Budget.filename)

        for subtable in ocd.Global_Carbon_Budget[version].Global_Budget[sheet_name]:
            csv_data = (
                ocd.Global_Carbon_Budget[version].Global_Budget[sheet_name][subtable]
                .to_dataframe()
                .to_csv()
            )
            subtable_slug = (
                subtable.lower()
                .replace(" ", "-")
                .replace("&", "")
                .replace("(", "")
                .replace(")", "")
                .replace("---", "-")
                .replace("--", "-")
                .replace("-net-does-not-include-peat-emissions", "")
            )
            filepath = f"data/global-carbon-budget-{version}-{slug}-{subtable_slug}.csv"
            print(filepath)

            with open(root / filepath, "w") as f:
                f.write(commented_notes)
                f.write(f"#\n# {subtable}\n")
                f.write(csv_data)

    for sheet_name in ocd.Global_Carbon_Budget[version].National_Fossil_Emissions:
        slug = sheet_name.lower().replace(" ", "-")
        notes = (
            ocd.Global_Carbon_Budget[version]
            .National_Fossil_Emissions[sheet_name]
            .__repr__()
        )
        commented_notes = comment_notes(
            notes, ocd.Global_Carbon_Budget[version].National_Fossil_Emissions.filename
        )
        csv_data = (
            ocd.Global_Carbon_Budget[version]
            .National_Fossil_Emissions[sheet_name]
            .to_dataframe()
            .to_csv()
        )

        filepath = f"data/national-fossil-emissions-{version}-{slug}.csv"
        print(filepath)

        with open(root / filepath, "w") as f:
            f.write(commented_notes)
            f.write(csv_data)

    if version >= "2022":
        for sheet_name in ocd.Global_Carbon_Budget[
            version
        ].National_Landuse_Change_Emissions:
            slug = sheet_name.lower().replace(" ", "-").replace("&", "")
            notes = (
                ocd.Global_Carbon_Budget[version]
                .National_Landuse_Change_Emissions[sheet_name]
                .__repr__()
            )
            commented_notes = comment_notes(
                notes,
                ocd.Global_Carbon_Budget[
                    version
                ].National_Landuse_Change_Emissions.filename,
            )
            csv_data = (
                ocd.Global_Carbon_Budget[version]
                .National_Landuse_Change_Emissions[sheet_name]
                .to_dataframe()
                .to_csv()
            )

            filepath = f"data/national-landuse-change-emissions-{version}-{slug}.csv"
            print(filepath)

            with open(root / filepath, "w") as f:
                f.write(commented_notes)
                f.write(csv_data)
