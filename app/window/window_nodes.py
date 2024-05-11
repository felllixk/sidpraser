from PyQt6.QtWidgets import QMainWindow, QPlainTextEdit, QPushButton, QTableWidget

from app.window.main_window import MainWindow


class WindowNodes:
    _window: MainWindow

    def __init__(self, window) -> None:
        self._window = window
        pass

    def getLogInput(self) -> QPlainTextEdit:
        return self._window.logInput

    def getLogOutput(self) -> QPlainTextEdit:
        return self._window.logOutput

    def getParseButton(self) -> QPushButton:
        return self._window.parseButton

    def getPushButtonClearLog(self) -> QPushButton:
        return self._window.pushButtonClearLog
    
    def getTableResult(self) -> QTableWidget:
        return self._window.tableWidgetResult
