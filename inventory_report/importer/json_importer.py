from inventory_report.importer.importer import Importer
from json import load


class JsonImporter(Importer):
    @classmethod
    def import_data(cls, path: str):
        try:
            inventory = []

            if not path.endswith(".json"):
                raise ValueError("Invalid file")

            with open(path) as file:
                data = load(file)

                for row in data:
                    inventory.append(row)

            return inventory

        except FileNotFoundError:
            print("File not found, check if the path is valid")
