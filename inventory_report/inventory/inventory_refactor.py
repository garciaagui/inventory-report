from collections.abc import Iterable
from inventory_report.inventory.inventory_iterator import InventoryIterator
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class InventoryRefactor(Iterable):
    def __init__(self, importer):
        self.importer = importer
        self.data = []

    def import_data(self, path: str, report_type: str):
        report = SimpleReport if report_type == "simples" else CompleteReport
        imported_data = self.importer.import_data(path)
        self.data.extend(imported_data)

        return report.generate(self.data)

    def __iter__(self):
        return InventoryIterator(self.data)
