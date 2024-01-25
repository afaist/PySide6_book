"""
https://www.pythonguis.com/tutorials/pyside6-bitmap-graphics/
QPainter and Bitmap Graphics
first stub application
"""
import sys
from PySide6 import QtGui
from PySide6.QtWidgets import QApplication, QLabel, QMainWindow
from PySide6.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QPainter")

        self.label = QLabel()
        canvas = QtGui.QPixmap(400, 300)
        canvas.fill(Qt.GlobalColor.white)
        self.label.setPixmap(canvas)
        self.setCentralWidget(self.label)
        self.draw_something()

    def draw_something(self):
        canvas = self.label.pixmap()
        painter = QtGui.QPainter(canvas)
        painter.drawLine(10, 10, 300, 200)
        painter.end()
        self.label.setPixmap(canvas)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
