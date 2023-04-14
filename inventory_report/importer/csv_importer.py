from inventory_report.importer.importer import Importer
from csv import DictReader


class CsvImporter(Importer):
    @classmethod
    def import_data(cls, path: str):
        try:
            inventory = []

            if not path.endswith(".csv"):
                raise ValueError("Invalid file")

            with open(path) as file:
                data = DictReader(file, delimiter=",", quotechar='"')

                for row in data:
                    inventory.append(row)

            return inventory

        except FileNotFoundError:
            print("File not found, check if the path is valid")
