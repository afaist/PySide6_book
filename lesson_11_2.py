"""
https://www.pythonguis.com/tutorials/pyside6-qprocess-external-programs/
Using QProcess to run external programs
Execute external program
"""
import sys

from PySide6.QtCore import QProcess, QSize
from PySide6.QtWidgets import (QApplication, QMainWindow, QPlainTextEdit,
                               QPushButton, QVBoxLayout, QWidget)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Run external programs")
        self.resize(QSize(400, 400))

        self.process = None

        self.btn = QPushButton("Execute")
        self.btn.pressed.connect(self.start_process)
        self.text = QPlainTextEdit()
        self.text.setReadOnly(True)

        layout = QVBoxLayout()
        layout.addWidget(self.btn)
        layout.addWidget(self.text)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def message(self, s):
        self.text.appendPlainText(s)

    def start_process(self):
        if self.process is None:
            self.message("Executing process.")
            self.process = QProcess()
            self.process.finished.connect(self.process_finished)
            self.process.start("python3", ["dummy_script.py"])

    def process_finished(self):
        self.message("Process finished.")
        self.process = None


app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec()
