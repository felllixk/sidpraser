from app.container import Container
from app.controllers import Controllers
from app.interface.i_kernel import IKernel
from app.logger import Logger


class Kernel(IKernel):
    container: Container
    controllers: Controllers

    def __init__(self) -> None:
        self.container = Container()
        self.controllers = Controllers(self.container)

    def run(self):
        self.container.register()
        self.container.boot()
        self.runQApplication()

    def runQApplication(self):
        qApp = self.container.getQApplication()
        window = self.container.getWindow()
        self.controllers.loadControllers()
        Logger.info('Приложение запущено')
        window.show()
        qApp.exec()

    def getWindow(self):
        return self.container.getWindow()

    def getContainer(self):
        return self.container

    def getControllers(self):
        return self.controllers
