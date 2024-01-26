"""
https://www.pythonguis.com/tutorials/pyside6-bitmap-graphics/
QPainter and Bitmap Graphics
Draw points
"""
import sys
from random import choice, randint

from PySide6 import QtGui
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QLabel, QMainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Draw points")

        self.label = QLabel()
        canvas = QtGui.QPixmap(400, 300)
        canvas.fill(Qt.GlobalColor.white)
        self.label.setPixmap(canvas)
        self.setCentralWidget(self.label)
        self.draw_something()

    def draw_something(self):
        colors = ['#FFD141', '#376F9F', '#0D1F2D', '#E9EBEF', '#EB5160']
        canvas = self.label.pixmap()
        painter = QtGui.QPainter(canvas)
        pen = QtGui.QPen()
        pen.setWidth(3)
        painter.setPen(pen)
        for n in range(10000):
            pen.setColor(QtGui.QColor(choice(colors)))
            painter.setPen(pen)
            painter.drawPoint(200 + randint(-100, 100), 150 + randint(-100, 100))

        pen.setWidth(40)
        pen.setColor(QtGui.QColor("red"))
        painter.setPen(pen)
        painter.drawPoint(200, 150)
        painter.end()
        self.label.setPixmap(canvas)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
