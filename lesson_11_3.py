"""
https://www.pythonguis.com/tutorials/pyside6-qprocess-external-programs/
Using QProcess to run external programs
Get data from external programs
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
            self.process.readyReadStandardOutput.connect(self.handle_stdout)
            self.process.readyReadStandardError.connect(self.handle_stderr)
            self.process.stateChanged.connect(self.handle_state)
            self.process.finished.connect(self.process_finished)
            self.process.start("python3", ["dummy_script.py"])

    def handle_stderr(self):
        if self.process is not None:
            data = self.process.readAllStandardError()
            stderr = data.toStdString()
            self.message(stderr)

    def handle_stdout(self):
        if self.process is not None:
            data = self.process.readAllStandardOutput()
            stdout = data.toStdString()
            self.message(stdout)

    def handle_state(self, state):
        states = {
            QProcess.ProcessState.NotRunning: "Not running",
            QProcess.ProcessState.Starting: "Starting",
            QProcess.ProcessState.Running: "Running",
        }
        state_name = states[state]
        self.message(f"State changed: {state_name}")

    def process_finished(self):
        self.message("Process finished.")
        self.process = None


app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec()
