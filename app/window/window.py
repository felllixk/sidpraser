from app.window.main_window import MainWindow
from app.window.window_nodes import WindowNodes


class Window:
    mainWindow: MainWindow
    nodes: WindowNodes

    def __init__(self, mainWindow: MainWindow):
        self.mainWindow = mainWindow
        self.mainWindow.loadUi()
        self.nodes = WindowNodes(self.mainWindow)

    def show(self) -> None:
        self.mainWindow.show()
