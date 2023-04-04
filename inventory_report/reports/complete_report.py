from inventory_report.reports.simple_report import SimpleReport
from collections import Counter


class CompleteReport(SimpleReport):
    def __get_companies_and_products_counter(products: "list[dict]") -> str:
        companies = [product["nome_da_empresa"] for product in products]
        companies_and_products_counter = list(Counter(companies).items())
        report = ""

        for company, products_counter in companies_and_products_counter:
            report += f"- {company}: {products_counter}\n"

        return report

    @classmethod
    def generate(cls, products: "list[dict]") -> str:
        simple_report = super().generate(products)
        products_counter = cls.__get_companies_and_products_counter(products)

        return (
            f"{simple_report}\n"
            f"Produtos estocados por empresa:\n"
            f"{products_counter}"
        )
