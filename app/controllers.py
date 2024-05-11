from app.container import Container
from controllers.LogController import LogController
from controllers.ParserController import ParserController
from controllers.TableResultController import TableResultController


class Controllers():
    def __init__(self, container: Container):
        self.container = container
        self.controllers = []

    def loadControllers(self):
        self.controllers.append(ParserController(self.container))
        self.controllers.append(LogController(self.container))
        self.controllers.append(TableResultController(self.container))
