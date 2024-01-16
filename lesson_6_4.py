"""
https://www.pythonguis.com/tutorials/pyside6-dialogs/
Dialogs
"""
import sys

from PySide6.QtCore import QSize
from PySide6.QtWidgets import (QApplication, QMainWindow, QMessageBox,
                               QPushButton, QVBoxLayout, QWidget)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Dialogs")
        self.setMinimumSize(QSize(400, 300))

        layout = QVBoxLayout()

        button = QPushButton("Press me for a message dialog!")
        button.clicked.connect(self.get_about_dialog)
        layout.addWidget(button)

        button = QPushButton("Press me for a critical dialog!")
        button.clicked.connect(self.get_critical_dialog)
        layout.addWidget(button)

        button = QPushButton("Press me for a information dialog!")
        button.clicked.connect(self.get_information_dialog)
        layout.addWidget(button)

        button = QPushButton("Press me for a question dialog!")
        button.clicked.connect(self.get_question_dialog)
        layout.addWidget(button)

        button = QPushButton("Press me for a warning dialog!")
        button.clicked.connect(self.get_warning_dialog)
        layout.addWidget(button)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def get_about_dialog(self, _):
        button = QMessageBox.about(
            self, "This is about dialog!", "You have a wonderfull day!")
        print(button)
        if button == QMessageBox.StandardButton.Ok:
            print("Yes!")
        else:
            print("No!")

    def get_critical_dialog(self, _):
        button = QMessageBox.critical(
            self, "This is critical dialog!", "Look up!!")
        if button == QMessageBox.StandardButton.Ok:
            print("Yes!")
        else:
            print("No!")

    def get_information_dialog(self, _):
        button = QMessageBox.information(
            self, "This is information dialog!", "Go up!!")
        if button == QMessageBox.StandardButton.Ok:
            print("Yes!")
        else:
            print("No!")

    def get_question_dialog(self, _):
        button = QMessageBox.question(
            self, "This is question dialog!", "Stand up?")
        if button == QMessageBox.StandardButton.Yes:
            print("Yes!")
        else:
            print("No!")

    def get_warning_dialog(self, _):
        button = QMessageBox.warning(
            self, "This is warning dialog!", "Everything is ok?")
        if button == QMessageBox.StandardButton.Ok:
            print("Yes!")
        else:
            print("No!")


app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec()
