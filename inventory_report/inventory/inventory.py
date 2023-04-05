from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
import csv
import json


class Inventory:
    def __read_csv(file, inventory):
        data = csv.DictReader(file, delimiter=",", quotechar='"')

        for row in data:
            inventory.append(row)

        return inventory

    def __read_json(file, inventory):
        data = json.load(file)

        for row in data:
            inventory.append(row)

        return inventory

    @classmethod
    def import_data(cls, path: str, report_type: str):
        report = SimpleReport if report_type == "simples" else CompleteReport

        try:
            inventory = []

            with open(path) as file:
                file_extension = path.split(".")[-1]

                if file_extension == "csv":
                    inventory = cls.__read_csv(file, inventory)

                else:
                    inventory = cls.__read_json(file, inventory)

            return report.generate(inventory)

        except FileNotFoundError:
            print("File not found, check if the path is valid")
