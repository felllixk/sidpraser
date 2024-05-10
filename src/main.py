import logging
from modules.Arguments import Arguments
from modules.LogParser import LogParser
from modules.SidAssociator import SidAssociator
from modules.SidParser import SidParser

logging.basicConfig(level=logging.INFO)


def main():
    args = Arguments()
    args.parseArguments()

    try:
        logging.info(f'Парсим сиды из лог файла: {args.logFilepath}')
        logParser = LogParser()
        logSids = logParser.parse(args.logFilepath)

        associator = SidAssociator(logSids)
        parser = SidParser(args.url)

        sidMap = parser.parse()

        associatedMap = associator.associateSid(sidMap)
        associator.storeResult(args.resultFilepath, associatedMap)
        logging.info(f'Результаты успешно сохранены в {args.resultFilepath}')
    except Exception as e:
        logging.error(f"Произошла ошибка: {e}")


if __name__ == "__main__":
    main()
