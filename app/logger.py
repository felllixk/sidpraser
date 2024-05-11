from PyQt6.QtWidgets import QPlainTextEdit


class Logger:
    logOutput: QPlainTextEdit | None = None

    @staticmethod
    def setLogOutput(logOutput: QPlainTextEdit):
        Logger.logOutput = logOutput

    @staticmethod
    def info(*values, sep=' '):
        # Формирование базового сообщения из аргументов
        base_message = sep.join(str(v) for v in values)
        # Добавление префикса [INFO]
        message = '[INFO]: ' + base_message
        Logger.log(message)

    @staticmethod
    def error(*values, sep=' '):
        # Формирование базового сообщения из аргументов
        base_message = sep.join(str(v) for v in values)
        # Добавление префикса [ERROR]
        message = '[ERROR]: ' + base_message
        Logger.log(message)

    @staticmethod
    def log(message: str):
        print(message)
        if Logger.logOutput is not None:
            Logger.logOutput.appendPlainText(message)
