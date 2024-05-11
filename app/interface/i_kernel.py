from abc import ABC, abstractmethod

from app.container import Container
from app.controllers import Controllers
from app.window.window import Window


class IKernel(ABC):
    @abstractmethod
    def getWindow(self) -> Window:
        pass

    @abstractmethod
    def getContainer(self) -> Container:
        pass

    @abstractmethod
    def getControllers(self) -> Controllers:
        pass

    @abstractmethod
    def run(self):
        pass
