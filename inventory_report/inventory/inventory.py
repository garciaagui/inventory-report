from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
import csv
import json


class Inventory:
    def __read_file(path: str, file):
        file_extension = path.split(".")[-1]

        if file_extension == "csv":
            return csv.DictReader(file, delimiter=",", quotechar='"')

        elif file_extension == "json":
            return json.load(file)

    @classmethod
    def import_data(cls, path: str, report_type: str):
        report = SimpleReport if report_type == "simples" else CompleteReport

        try:
            invetory = []

            with open(path) as file:
                data = cls.__read_file(path, file)

                for row in data:
                    invetory.append(row)

            return report.generate(invetory)

        except FileNotFoundError:
            print("File not found, check if the path is valid")


print(Inventory.import_data("inventory_report/data/inventory.json", "simples"))
