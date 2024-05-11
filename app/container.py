
from app.logger import Logger
from app.window.window import Window
from app.window.main_window import MainWindow
from PyQt6.QtWidgets import QApplication


class Container:
    services: dict[object] = {}

    def register(self):
        self.services['q_app'] = QApplication([])
        self.services['window'] = Window(MainWindow())

    def boot(self):
        Logger.setLogOutput(self.getWindow().nodes.getLogOutput())

    def getWindow(self) -> Window:
        return self.services['window']

    def getQApplication(self) -> QApplication:
        return self.services['q_app']
