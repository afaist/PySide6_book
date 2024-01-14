"""
Lesson 3
https://www.pythonguis.com/tutorials/pyside6-widgets/
Виджеты
QCheckBox
"""
import sys

from PySide6.QtWidgets import (QApplication, QCheckBox, QMainWindow,
                               QVBoxLayout, QWidget)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QCheckBox App")

        layout = QVBoxLayout()

        checkbox_big = QCheckBox("Three states")
        font = checkbox_big.font()
        font.setPointSize(30)
        checkbox_big.setFont(font)
        checkbox_big.setStyleSheet("color: blue")
        checkbox_big.setTristate(True)

        checkbox_small = QCheckBox("Two states")
        checkbox_small.setStyleSheet("color: green")

        layout.addWidget(checkbox_big)
        layout.addWidget(checkbox_small)

        central_widget = QWidget()
        central_widget.setLayout(layout)

        self.setCentralWidget(central_widget)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
