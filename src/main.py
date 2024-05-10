import logging
from modules.arguments import Arguments
from modules.log_parser import LogParser
from modules.sid_associator import SidAssociator
from modules.sid_parser import SidParser
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
