from inventory_report.inventory.product import Product


def test_cria_produto():
    new_product = Product(
        11,
        "Mark III",
        "Stark Industries",
        "2023-04-04",
        "2025-04-04",
        "FR29 5791 5333 58XR G4PR IG28 D08",
        "Tony Stark confidential data",
    )

    assert new_product.id == 11
    assert new_product.nome_do_produto == "Mark III"
    assert new_product.nome_da_empresa == "Stark Industries"
    assert new_product.data_de_fabricacao == "2023-04-04"
    assert new_product.data_de_validade == "2025-04-04"
    assert new_product.numero_de_serie == "FR29 5791 5333 58XR G4PR IG28 D08"
    assert (
        new_product.instrucoes_de_armazenamento
        == "Tony Stark confidential data"
    )
