import os
import sys
from PyQt6.QtWidgets import QMainWindow
from PyQt6.uic import loadUi
from app.file_resolver import FileResolver


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

    def loadUi(self):
        loadUi(FileResolver.getPath('resource/sidparser.ui'), self)
        self.setWindowTitle("Sid Parser")
