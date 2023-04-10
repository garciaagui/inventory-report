import sys
from inventory_report.inventory.inventory_refactor import Inventory
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter


def generate_report(path: str, report_type: str):
    if path.endswith(".csv"):
        return Inventory(CsvImporter).import_data(path, report_type)

    elif path.endswith(".json"):
        return Inventory(JsonImporter).import_data(path, report_type)

    elif path.endswith(".xml"):
        return Inventory(XmlImporter).import_data(path, report_type)

    else:
        raise ValueError("Arquivo inválido")


def main():
    try:
        _, path, report_type = sys.argv

        report = generate_report(path, report_type)

        print(report, end="")

    except ValueError:
        print("Verifique os argumentos", file=sys.stderr)
