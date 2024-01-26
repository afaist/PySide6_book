"""
https://www.pythonguis.com/tutorials/pyside6-bitmap-graphics/
QPainter and Bitmap Graphics
DrawLine, drawRect, drawRects and drawRoundedRect
"""
import sys
from random import choice, randint

from PySide6 import QtGui
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QLabel, QMainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Draw rects")
        self.resize(400, 400)

        self.label = QLabel()
        canvas = QtGui.QPixmap(400, 350)
        canvas.fill(Qt.GlobalColor.white)
        self.label.setPixmap(canvas)
        self.setCentralWidget(self.label)
        self.draw_something()

    def draw_something(self):
        colors = ["#FFD141", "#376F9F", "#0D1F2D", "#19FBBB", "#EB5160"]
        canvas = self.label.pixmap()
        painter = QtGui.QPainter(canvas)
        pen = QtGui.QPen()
        pen.setWidth(5)
        painter.setPen(pen)
        brush = QtGui.QBrush()
        brush.setStyle(Qt.BrushStyle.Dense1Pattern)
        for _ in range(10):
            pen.setColor(QtGui.QColor(choice(colors)))
            painter.setPen(pen)
            brush.setColor(QtGui.QColor(choice(colors)))
            painter.setBrush(brush)
            painter.drawRoundedRect(
                randint(0, 100),
                randint(0, 100),
                randint(100, 250),
                randint(100, 250),
                30,
                30
            )

        pen.setWidth(40)
        pen.setColor(QtGui.QColor("red"))
        painter.setPen(pen)
        painter.drawPoint(300, 150)
        painter.end()
        self.label.setPixmap(canvas)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
