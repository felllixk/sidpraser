from app.container import Container
from app.interface.i_kernel import IKernel
from app.window.window import Window


class App:
    kernel: IKernel = None

    @staticmethod
    def setKernel(kernel: IKernel):
        App.kernel = kernel

    @staticmethod
    def getKernel() -> IKernel:
        return App.kernel

    @staticmethod
    def getWindow() -> Window:
        return App.kernel.getWindow()

    @staticmethod
    def getContainer() -> Container:
        return App.kernel.getContainer()

    @staticmethod
    def run() -> Container:
        return App.kernel.run()
