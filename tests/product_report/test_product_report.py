from inventory_report.inventory.product import Product


def test_relatorio_produto(capsys):
    new_product = Product(
        11,
        "Mark III",
        "Stark Industries",
        "2023-04-04",
        "2025-04-04",
        "FR29 5791 5333 58XR G4PR IG28 D08",
        "longe do Thanos",
    )

    expected_print_output = (
        f"O produto {new_product.nome_do_produto}"
        f" fabricado em {new_product.data_de_fabricacao}"
        f" por {new_product.nome_da_empresa} com validade"
        f" até {new_product.data_de_validade}"
        f" precisa ser armazenado {new_product.instrucoes_de_armazenamento}.\n"
    )

    print(new_product)
    captured, _ = capsys.readouterr()

    assert expected_print_output == captured
