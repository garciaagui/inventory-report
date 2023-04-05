from inventory_report.reports.colored_report import ColoredReport
from inventory_report.reports.simple_report import SimpleReport


def test_decorar_relatorio(capsys):
    mocked_data = [
        {
            "id": "1",
            "nome_do_produto": "Nicotine Polacrilex",
            "nome_da_empresa": "Target Corporation",
            "data_de_fabricacao": "2021-02-18",
            "data_de_validade": "2023-09-17",
            "numero_de_serie": "CR25 1551 4467 2549 4402 1",
            "instrucoes_de_armazenamento": "instrucao 1",
        },
        {
            "id": "2",
            "nome_do_produto": "fentanyl citrate",
            "nome_da_empresa": "Target Corporation",
            "data_de_fabricacao": "2020-12-06",
            "data_de_validade": "2023-12-25",
            "numero_de_serie": "FR29 5951 7573 74OY XKGX 6CSG D20",
            "instrucoes_de_armazenamento": "instrucao 2",
        },
        {
            "id": "3",
            "nome_do_produto": "NITROUS OXIDE",
            "nome_da_empresa": "Galena Biopharma",
            "data_de_fabricacao": "2020-12-22",
            "data_de_validade": "2024-11-07",
            "numero_de_serie": "CZ09 8588 0858 8435 9140 2695",
            "instrucoes_de_armazenamento": "instrucao 3",
        },
    ]
    print(ColoredReport(SimpleReport).generate(mocked_data))

    def green(sentence):
        return f"\033[32m{sentence}\033[0m"

    def blue(sentence):
        return f"\033[36m{sentence}\033[0m\n"

    def red(sentence):
        return f"\033[31m{sentence}\033[0m\n"

    expected_print_output = (
        f"{green('Data de fabricação mais antiga:')} {blue('2020-12-06')}"
        f"{green('Data de validade mais próxima:')} {blue('2023-09-17')}"
        f"{green('Empresa com mais produtos:')} {red('Target Corporation')}"
    )

    captured, _ = capsys.readouterr()

    assert expected_print_output == captured
