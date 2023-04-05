from inventory_report.importer.importer import Importer
from json import load


class JsonImporter(Importer):
    @classmethod
    def import_data(cls, path: str):
        try:
            file_extension = path.split(".")[-1]
            inventory = []

            if file_extension != "json":
                raise ValueError("Arquivo inválido")

            with open(path) as file:
                data = load(file)

                for row in data:
                    inventory.append(row)

            return inventory

        except FileNotFoundError:
            print("File not found, check if the path is valid")
