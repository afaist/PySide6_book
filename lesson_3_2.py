"""
Lesson 3
https://www.pythonguis.com/tutorials/pyside6-widgets/
Виджеты
QLabel
"""
import sys

from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QVBoxLayout,
                               QWidget)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QLabel App")

        layout = QVBoxLayout()

        label_text = QLabel("Picture show")
        font = label_text.font()
        font.setPointSize(30)
        label_text.setFont(font)

        label_text.setAlignment(
            Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter
        )
        label_png = QLabel()
        label_png.setPixmap(QPixmap("01.png"))

        layout.addWidget(label_text)
        layout.addWidget(label_png)

        central_widget = QWidget()
        central_widget.setLayout(layout)

        self.setCentralWidget(central_widget)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
