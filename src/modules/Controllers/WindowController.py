from abc import ABC, abstractmethod

from app.kernel import Kernel
from modules.Window.Window import Window


class WindowController(ABC):
    application: Kernel
    window: Window

    def __init__(self):
        self.window = Kernel.getContainer().getWindow()

    @abstractmethod
    def registerAction(self):
        pass
