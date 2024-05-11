from modules.Controllers.ParserController import ParserController


class WindowControllers:
    controllers = [
        ParserController()
    ]

    def bootControllers(self):
        for controller in self.controllers:
            controller.registerAction()
