from inventory_report.inventory.product import Product


def test_product_report_by_print(capsys):
    new_product = Product(
        11,
        "Mark III",
        "Stark Industries",
        "2023-04-04",
        "2025-04-04",
        "FR29 5791 5333 58XR G4PR IG28 D08",
        "away from Thanos",
    )

    expected_print_output = (
        f"The product {new_product.nome_do_produto}"
        f" manufactured in {new_product.data_de_fabricacao}"
        f" by {new_product.nome_da_empresa} valid"
        f" until {new_product.data_de_validade}"
        f" needs to be stored {new_product.instrucoes_de_armazenamento}.\n"
    )

    print(new_product)
    captured, _ = capsys.readouterr()

    assert expected_print_output == captured
