from inventory_report.importer.importer import Importer
from csv import DictReader


class CsvImporter(Importer):
    @classmethod
    def import_data(cls, path: str):
        try:
            file_extension = path.split(".")[-1]
            inventory = []

            if file_extension != "csv":
                raise ValueError("Arquivo inválido")

            with open(path) as file:
                data = DictReader(file, delimiter=",", quotechar='"')

                for row in data:
                    inventory.append(row)

            return inventory

        except FileNotFoundError:
            print("File not found, check if the path is valid")
