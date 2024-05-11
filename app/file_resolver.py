import os
import sys


class FileResolver:
    @staticmethod
    def getPath(filepath: str) -> str:
        if getattr(sys, 'frozen', False):
            # Если приложение запущено из собранного исполняемого файла
            return os.path.join(sys._MEIPASS, filepath)
        else:
            return filepath
