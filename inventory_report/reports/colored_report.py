import re
from ..reports.complete_report import CompleteReport


class ColoredReport(CompleteReport):
    @classmethod
    def generate(cls, products: "list[dict]") -> str:
        report = super().generate(products)

        index_start = report.find("more products:") + 15
        index_finish = report.find("\n", index_start)
        if index_finish == -1:
            index_finish = len(report)

        report = (
            report[:index_start]
            + "\033[31m"
            + report[index_start:index_finish]
            + "\033[0m"
            + report[index_finish:]
        )

        green_phrases = [
            "Oldest manufacturing date:",
            "Nearest expiration date:",
            "Company with more products:",
        ]

        for phrase in green_phrases:
            report = report.replace(
                phrase,
                f"\033[32m{phrase}\033[0m",
            )

        report_dates = re.findall(r"(\d+-\d+-\d+)", report)

        for date in report_dates:
            report = report.replace(
                date,
                f"\033[36m{date}\033[0m",
            )

        return report
