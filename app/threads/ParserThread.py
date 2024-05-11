from PyQt6.QtCore import QThread, pyqtSignal

from app.logger import Logger
from app.parser.log_parser import LogParser
from app.parser.sid_associator import SidAssociator
from app.parser.sid_parser import SidParser


class ParserThread(QThread):
    finished = pyqtSignal(dict, str)

    def __init__(self, logs: str, url: str):
        super().__init__()
        self.url = url
        self.logs = logs

    def run(self):
        try:
            # Парсинг логов
            list_of_strings = self.logs.split('\n')
            logParser = LogParser()
            hexes = logParser.parseHexes(list_of_strings)
            hexes = logParser.unifyLines(hexes)
            logSids = logParser.parseSids(hexes)
            Logger.info('Результат парсинга логов:', logSids)

            # Парсинг сайта
            sidParser = SidParser(self.url)
            Logger.info('Отправка запроса: на ' + self.url)
            siteSids = sidParser.parse()
            Logger.info('Получены сиды:', siteSids)

            # Ассоциация
            associator = SidAssociator()
            result = associator.associateSid(siteSids, logSids)
            Logger.info('Найдено пересечение:', result)
            self.finished.emit(result, "")
        except Exception as e:
            # Передаем пустой словарь и сообщение об ошибке
            self.finished.emit({}, str(e))
