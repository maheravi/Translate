# This Python file uses the following encoding: utf-8
import sys
from functools import partial
from PySide6.QtWidgets import QApplication, QWidget, QMessageBox
from PySide6.QtUiTools import QUiLoader
import random


class Main(QWidget):
    def __init__(self):
        super(Main, self).__init__()

        loader = QUiLoader()
        self.ui = loader.load("form.ui")
        self.ui.show()
        self.ui.translate.clicked.connect(self.translate)
        self.setWindowTitle("My Translator")

    def translate(self):
        f = open('translate.csv')
        big_text = f.read()
        parts = big_text.split('\n')
        words = []
        for word in parts:
            words.append(word)
        if self.ui.ftoe.isChecked():
            a = self.ui.box1.text()
            for i in range(len(words)):
                if words[i] == a:
                    self.ui.result.setText(words[i-1])

        elif self.ui.etof.isChecked():
            a = self.ui.box1.text()
            for i in range(len(words)):
                if words[i] == a:
                    self.ui.result.setText(words[i+1])


if __name__ == "__main__":
    app = QApplication([])
    window = Main()
    # window.show()
    sys.exit(app.exec_())
