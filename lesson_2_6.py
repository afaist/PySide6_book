"""
Lesson 2
https://www.pythonguis.com/tutorials/pyside6-signals-slots-events/
Signals, Slots & Events and get Data, storing Data
Соединение виджетов напрямую
"""
# Only needed for access to command line arguments
import sys

from PySide6.QtCore import QSize
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
                               QVBoxLayout, QWidget)


# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Мое приложение")

        self.label = QLabel()
        self.input = QLineEdit()
        self.input.textChanged.connect(self.label.setText)

        layout = QVBoxLayout()
        layout.addWidget(self.input)
        layout.addWidget(self.label)

        container = QWidget()
        container.setLayout(layout)

        self.setMinimumSize(QSize(400, 300))
        self.setCentralWidget(container)


# You need one (and only one) QApplication isinstance per application.
# Pass in sys.argv to allow command line arguments for your app.
# If you know yow won't use command line arguments QApplication([]) works too.
app = QApplication(sys.argv)
# Create a Qt widget, which will be our window.
window = MainWindow()
window.show()  # IMPORTANT!!! Windows are hidden by default.
# Start the event loop.
app.exec()
