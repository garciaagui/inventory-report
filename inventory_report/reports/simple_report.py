from abc import ABC, abstractmethod
from datetime import datetime, date
from collections import Counter


class BaseReport(ABC):
    @abstractmethod
    def generate(cls, products: "list[dict]") -> str:
        raise NotImplementedError


class SimpleReport:
    def __get_oldest_manufacturing_date(products: "list[dict]") -> str:
        oldest_date = products[0]["data_de_fabricacao"]

        for product in products:
            if product["data_de_fabricacao"] < oldest_date:
                oldest_date = product["data_de_fabricacao"]

        return oldest_date

    def __get_unexpired_products(products: "list[dict]") -> "list[dict]":
        today = date.today()
        unexpired_products = []

        for product in products:
            current_product_date = datetime.strptime(
                product["data_de_validade"], "%Y-%m-%d"
            ).date()

            if current_product_date >= today:
                unexpired_products.append(product)

        return unexpired_products

    def __get_nearest_expiration_date(cls, products: "list[dict]") -> date:
        unexpired_products = cls.__get_unexpired_products(products)

        nearest_date = unexpired_products[0]["data_de_validade"]

        for product in unexpired_products:
            if product["data_de_validade"] < nearest_date:
                nearest_date = product["data_de_validade"]

        return nearest_date

    def __get_company_with_more_products(products: "list[dict]") -> str:
        companies = [product["nome_da_empresa"] for product in products]
        company_with_more_products, _ = Counter(companies).most_common()[0]

        return company_with_more_products

    @classmethod
    def generate(cls, products: "list[dict]") -> str:
        oldest_date = cls.__get_oldest_manufacturing_date(products)
        nearest_date = cls.__get_nearest_expiration_date(cls, products)
        company = cls.__get_company_with_more_products(products)

        return (
            f"Oldest manufacturing date: {oldest_date}\n"
            f"Nearest expiration date: {nearest_date}\n"
            f"Company with more products: {company}"
        )
