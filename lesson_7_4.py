"""
https://www.pythonguis.com/tutorials/pyside6-creating-multiple-windows/
Creating additional windows
Two another windows with lambda
"""

import sys
from random import randint

from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QPushButton,
                               QVBoxLayout, QWidget)


class AnotherWindow(QWidget):
    """
    This window is a QWidget. If it has no parent, it will
    appear as a free-floating window as we want.
    """

    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.label = QLabel("Another window %d" % randint(0, 100))
        layout.addWidget(self.label)
        self.setLayout(layout)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.window1 = AnotherWindow()
        self.window2 = AnotherWindow()

        layout = QVBoxLayout()

        button = QPushButton("Push for Window 1")
        button.clicked.connect(lambda: self.toggle_window(self.window1))
        layout.addWidget(button)

        button = QPushButton("Push for Window 2")
        button.clicked.connect(lambda: self.toggle_window(self.window2))
        layout.addWidget(button)

        w = QWidget()
        w.setLayout(layout)
        self.setCentralWidget(w)

    def toggle_window(self, window):
        if window.isVisible():
            window.hide()
        else:
            window.show()


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
