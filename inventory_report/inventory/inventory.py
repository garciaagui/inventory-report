from collections.abc import Iterable
from ..inventory.inventory_iterator import InventoryIterator
from ..reports.simple_report import SimpleReport
from ..reports.complete_report import CompleteReport
from ..reports.colored_report import ColoredReport


class Inventory(Iterable):
    def __init__(self, importer):
        self.importer = importer
        self.data = []

    def __define_report(self, report_type: str):
        reports = dict(
            simple=SimpleReport,
            complete=CompleteReport,
            colored=ColoredReport,
        )

        if report_type not in reports:
            raise ValueError("Report type must be simple, complete or colored")

        return reports[report_type]

    def import_data(self, path: str, report_type: str):
        report = self.__define_report(report_type)
        imported_data = self.importer.import_data(path)
        self.data.extend(imported_data)

        return report.generate(self.data)

    def __iter__(self):
        return InventoryIterator(self.data)
