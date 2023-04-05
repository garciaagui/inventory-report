from inventory_report.importer.importer import Importer
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
from csv import DictReader


class CsvImporter(Importer):
    @classmethod
    def import_data(cls, path: str, report_type: str):
        report = SimpleReport if report_type == "simples" else CompleteReport

        try:
            file_extension = path.split(".")[-1]
            inventory = []

            if file_extension != "csv":
                raise ValueError("Arquivo inválido")

            with open(path) as file:
                data = DictReader(file, delimiter=",", quotechar='"')

                for row in data:
                    inventory.append(row)

            return report.generate(inventory)

        except FileNotFoundError:
            print("File not found, check if the path is valid")
