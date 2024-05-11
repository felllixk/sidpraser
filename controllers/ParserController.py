from typing import Any
from app.container import Container
from app.logger import Logger
from app.table_manager import TableManager
from app.threads.ParserThread import ParserThread


class ParserController:
    def __init__(self, container: Container):
        self.window = container.getWindow()
        self.setup_connections()
        self.tableManager = TableManager(self.window.nodes.getTableResult())

    def setup_connections(self):
        self.window.nodes.getParseButton().clicked.connect(self.on_button_clicked)

    def on_button_clicked(self):
        parseButton = self.window.nodes.getParseButton()
        parseButton.setEnabled(False)

        logs = self.window.nodes.getLogInput().toPlainText()
        self.parser_thread = ParserThread(
            logs, 'https://www.lyngsat.com/packages/Telekarta-80E.html')
        self.parser_thread.finished.connect(self.on_parsing_finished)
        self.parser_thread.start()

    

    def on_parsing_finished(self, siteSids: dict[str | None, Any], error):
        if error:
            Logger.error('Ошибка при парсинге:', error)
        parseButton = self.window.nodes.getParseButton()

        result = []
        for sid, channel in siteSids.items():
            result.append([sid, channel])

        self.tableManager.set_data(result)
        parseButton.setEnabled(True)
