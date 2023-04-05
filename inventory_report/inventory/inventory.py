from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
import csv
import json
import xml.etree.ElementTree as ET


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

    def __read_xml(file, inventory):
        tree = ET.parse(file)
        root = tree.getroot()

        for record in root.findall("record"):
            product = dict(
                id=record.find("id").text,
                nome_do_produto=record.find("nome_do_produto").text,
                nome_da_empresa=record.find("nome_da_empresa").text,
                data_de_fabricacao=record.find("data_de_fabricacao").text,
                data_de_validade=record.find("data_de_validade").text,
                numero_de_serie=record.find("numero_de_serie").text,
                instrucoes_de_armazenamento=record.find(
                    "instrucoes_de_armazenamento"
                ).text,
            )

            inventory.append(product)

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

                elif file_extension == "json":
                    inventory = cls.__read_json(file, inventory)

                else:
                    inventory = cls.__read_xml(file, inventory)

            return report.generate(inventory)

        except FileNotFoundError:
            print("File not found, check if the path is valid")
