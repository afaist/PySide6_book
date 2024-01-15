"""
https://www.pythonguis.com/tutorials/pyside6-layouts/
Макеты
QStackedLayout
"""
import sys

from PySide6.QtCore import QSize
from PySide6.QtGui import QColor, QPalette
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QMainWindow,
                               QPushButton, QStackedLayout, QVBoxLayout,
                               QWidget)


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("Stacked Layout")
        self.setMinimumSize(QSize(400, 300))

        page_layout = QVBoxLayout()
        button_layout = QHBoxLayout()

        self.stack_layout = QStackedLayout()

        page_layout.addLayout(button_layout)
        page_layout.addLayout(self.stack_layout)

        btn = QPushButton("red")
        btn.setStyleSheet("background-color: red")
        btn.pressed.connect(self.activate_tab_1)
        button_layout.addWidget(btn)
        self.stack_layout.addWidget(Color("red"))  # stack 0

        btn = QPushButton("green")
        btn.setStyleSheet("background-color: green")
        btn.pressed.connect(self.activate_tab_2)
        button_layout.addWidget(btn)
        self.stack_layout.addWidget(Color("green"))  # stack 1

        btn = QPushButton("yellow")
        btn.setStyleSheet("background-color: yellow")
        btn.pressed.connect(self.activate_tab_3)
        button_layout.addWidget(btn)
        self.stack_layout.addWidget(Color("yellow"))  # stack 2

        widget = QWidget()
        widget.setLayout(page_layout)
        self.setCentralWidget(widget)

    def activate_tab_1(self):
        self.stack_layout.setCurrentIndex(0)

    def activate_tab_2(self):
        self.stack_layout.setCurrentIndex(1)

    def activate_tab_3(self):
        self.stack_layout.setCurrentIndex(2)


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
