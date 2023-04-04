from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
import csv


class Inventory:
    @classmethod
    def import_data(cls, path: str, report_type: str):
        report = SimpleReport if report_type == "simples" else CompleteReport

        try:
            invetory = []

            with open(path) as file:
                data = csv.DictReader(file, delimiter=",", quotechar='"')

                for row in data:
                    invetory.append(row)

            return report.generate(invetory)

        except FileNotFoundError:
            print("File not found, check if the path is valid")
