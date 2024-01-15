"""
https://www.pythonguis.com/tutorials/pyside6-layouts/
Макеты
Nesting Layouts
"""
import sys

from PySide6.QtCore import QSize
from PySide6.QtGui import QColor, QPalette
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QMainWindow,
                               QVBoxLayout, QWidget)


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("Nesting BoxLayout")
        self.setMinimumSize(QSize(400, 300))

        layout1 = QHBoxLayout()
        layout2 = QVBoxLayout()
        layout3 = QVBoxLayout()

        layout1.setContentsMargins(10, 0, 0, 0)
        layout1.setSpacing(20)
        layout1.addWidget(QLabel("Layout 1"))

        layout2.addWidget(QLabel("Layout 2"))
        layout2.addWidget(Color("red"))
        layout2.addWidget(Color("green"))
        layout2.addWidget(Color("blue"))

        layout1.addLayout(layout2)

        layout3.addWidget(QLabel("Layout 3"))
        layout3.addWidget(Color("yellow"))
        layout3.addWidget(Color("purple"))

        layout1.addLayout(layout3)

        widget = QWidget()
        widget.setLayout(layout1)
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
