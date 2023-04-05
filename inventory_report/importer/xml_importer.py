from inventory_report.importer.importer import Importer
import xml.etree.ElementTree as ET


class XmlImporter(Importer):
    @classmethod
    def import_data(cls, path: str):
        try:
            file_extension = path.split(".")[-1]
            inventory = []

            if file_extension != "xml":
                raise ValueError("Arquivo inválido")

            with open(path) as file:
                tree = ET.parse(file)
                root = tree.getroot()

                for record in root.findall("record"):
                    product = dict(
                        id=record.find("id").text,
                        nome_do_produto=record.find("nome_do_produto").text,
                        nome_da_empresa=record.find("nome_da_empresa").text,
                        data_de_fabricacao=record.find(
                            "data_de_fabricacao"
                        ).text,
                        data_de_validade=record.find("data_de_validade").text,
                        numero_de_serie=record.find("numero_de_serie").text,
                        instrucoes_de_armazenamento=record.find(
                            "instrucoes_de_armazenamento"
                        ).text,
                    )

                    inventory.append(product)

            return inventory

        except FileNotFoundError:
            print("File not found, check if the path is valid")
