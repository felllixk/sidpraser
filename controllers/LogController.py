from app.container import Container


class LogController:
    def __init__(self, container: Container):
        self.window = container.getWindow()
        self.setup_connections()

    def setup_connections(self):
        self.window.nodes.getPushButtonClearLog().clicked.connect(self.on_button_clicked)

    def on_button_clicked(self):
        self.window.nodes.getLogOutput().setPlainText('')
