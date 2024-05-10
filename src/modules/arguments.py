import argparse


class Arguments():
    logFilepath: str
    resultFilepath: str
    url: str

    def __init__(self) -> None:
        pass

    def parseArguments(self) -> None:
        parser = argparse.ArgumentParser(
            description="Парсит данные с сайта и сохраняет результаты в файл.")
        parser.add_argument(
            "-log",
            required=True,
            help="Путь к файлу с Сидами для проверки.",
            type=str
        )
        parser.add_argument(
            "-url",
            default="https://www.lyngsat.com/packages/Telekarta-80E.html",
            help="Путь к файлу результатов.",
            type=str
        )
        parser.add_argument(
            "-result",
            default="result.txt",
            help="Путь к файлу результатов.",
            type=str
        )
        args = parser.parse_args()

        self.logFilepath = args.log
        self.resultFilepath = args.result
        self.url = args.url
