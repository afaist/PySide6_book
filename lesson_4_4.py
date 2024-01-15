"""
https://www.pythonguis.com/tutorials/pyside6-layouts/
Макеты
QGridLayout
"""
import sys

from PySide6.QtCore import QSize
from PySide6.QtGui import QColor, QPalette
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QMainWindow,
                               QWidget)


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("Grid Layout")
        self.setMinimumSize(QSize(400, 300))

        layout = QGridLayout()

        layout.setContentsMargins(10, 0, 0, 0)
        layout.setSpacing(20)
        layout.addWidget(QLabel("Grid Layout"), 0, 0)

        layout.addWidget(Color("red"), 1, 0)
        layout.addWidget(Color("green"), 1, 1)
        layout.addWidget(Color("blue"), 2, 0)

        layout.addWidget(QLabel("Layout 3"), 2, 1)
        layout.addWidget(Color("yellow"), 2, 2)
        layout.addWidget(Color("purple"), 3, 1)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)


class Color(QWidget):
    """
    Вспомогательный класс для вывода цветных полос
    """

    def __init__(self, color):
        super(Color, self).__init__()
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor(color))
        self.setPalette(palette)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
