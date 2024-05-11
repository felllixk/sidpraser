from modules.Controllers.WindowController import WindowController


class ParserController(WindowController):
    def registerAction(self):
        logInput = self.window.nodes.getParseButton()
        logInput.clicked.connect(self.parse)

    def parse(self):
        logText = self.window.nodes.getLogInput()
        print("Кнопка 'Парсить' нажата")
        print(logText)
