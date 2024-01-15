"""
https://www.pythonguis.com/tutorials/pyside6-layouts/
Макеты
QTabWidget
"""
import sys

from PySide6.QtCore import QSize
from PySide6.QtGui import QColor, QPalette
from PySide6.QtWidgets import QApplication, QMainWindow, QTabWidget, QWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("Stacked Layout")
        self.setMinimumSize(QSize(400, 300))

        tabs = QTabWidget()
        tabs.setTabPosition(QTabWidget.TabPosition.West)
        tabs.setMovable(True)

        for _, color in enumerate(["red", "green", "blue", "yellow"]):
            tabs.addTab(Color(color), color)

        self.setCentralWidget(tabs)


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
