"""
https://www.pythonguis.com/tutorials/pyside6-bitmap-graphics/
QPainter and Bitmap Graphics
Draw with mouse
"""
import sys

from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QLabel, QMainWindow


class Canvas(QLabel):
    def __init__(self):
        super().__init__()

        pixmap = QtGui.QPixmap(600, 300)
        pixmap.fill(Qt.GlobalColor.white)
        self.setPixmap(pixmap)

        self.last_x, self.last_y = None, None
        self.pen_color = QtGui.QColor("#000000")

    def set_pen_color(self, color):
        self.pen_color = QtGui.QColor(color)

    def mouseMoveEvent(self, ev):
        pos_x = int(ev.position().x())
        pos_y = int(ev.position().y())
        if self.last_x is None or self.last_y is None:  # First event
            self.last_x = pos_x
            self.last_y = pos_y
        else:
            canvas = self.pixmap()
            painter = QtGui.QPainter(canvas)
            pen = painter.pen()
            pen.setWidth(4)
            pen.setColor(self.pen_color)
            painter.setPen(pen)
            painter.drawLine(self.last_x, self.last_y, pos_x, pos_y)
            painter.end()
            self.setPixmap(canvas)
            # Update the origin for next time.
            self.last_x = pos_x
            self.last_y = pos_y

    def mouseReleaseEvent(self, ev):
        self.last_x = None
        self.last_y = None


COLORS = [
    # 17 undertones https://lospec.com/palette-list/17undertones
    "#000000",
    "#141923",
    "#414168",
    "#3a7fa7",
    "#35e3e3",
    "#8fd970",
    "#5ebb49",
    "#458352",
    "#dcd37b",
    "#fffee5",
    "#ffd035",
    "#cc9245",
    "#a15c3e",
    "#a42f3b",
    "#f45b7a",
    "#c24998",
    "#81588d",
    "#bcb0c2",
    "#ffffff",
]


class QPaletteButton(QtWidgets.QPushButton):
    def __init__(self, color):
        super().__init__()
        self.setFixedSize(QtCore.QSize(24, 24))
        self.color = color
        self.setStyleSheet("background-color: %s;" % color)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.canvas = Canvas()

        w = QtWidgets.QWidget()
        layout = QtWidgets.QVBoxLayout()
        w.setLayout(layout)
        layout.addWidget(self.canvas)

        palette = QtWidgets.QHBoxLayout()
        self.add_palette_buttons(palette)
        layout.addLayout(palette)

        self.setCentralWidget(w)

    def add_palette_buttons(self, layout):
        for c in COLORS:
            b = QPaletteButton(c)
            b.pressed.connect(lambda c=c: self.canvas.set_pen_color(c))
            layout.addWidget(b)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
print(window.size())
app.exec()
