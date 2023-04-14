import sys
from inventory_report.inventory.inventory import Inventory
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter


def generate_report(path: str, report_type: str):
    file_extension = path.split(".")[-1]
    importers = dict(csv=CsvImporter, json=JsonImporter, xml=XmlImporter)

    if file_extension not in importers:
        raise ValueError("Invalid file")

    return Inventory(importers[file_extension]).import_data(path, report_type)


def main():
    try:
        _, path, report_type = sys.argv

        report = generate_report(path, report_type)

        print(report, end="")

    except ValueError:
        print("Check the arguments", file=sys.stderr)
