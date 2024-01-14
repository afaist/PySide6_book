"""
Lesson 3
https://www.pythonguis.com/tutorials/pyside6-widgets/
Виджеты
QComboBox
"""
import sys

from PySide6.QtWidgets import (QApplication, QComboBox, QMainWindow,
                               QVBoxLayout, QWidget)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QComboBox App")

        layout = QVBoxLayout()

        combobox_big = QComboBox()
        font = combobox_big.font()
        font.setPointSize(30)
        combobox_big.setFont(font)
        combobox_big.setStyleSheet("color: blue")
        combobox_big.addItems(["One", "Two", "Three", "Four"])

        combobox_big.currentIndexChanged.connect(self.index_changed)
        combobox_big.currentTextChanged.connect(self.text_changed)

        combobox_small = QComboBox()
        combobox_small.setStyleSheet("color: green")
        combobox_small.addItems(["First", "Second"])

        layout.addWidget(combobox_big)
        layout.addWidget(combobox_small)

        central_widget = QWidget()
        central_widget.setLayout(layout)

        self.setCentralWidget(central_widget)

    def index_changed(self, index):
        print(f"Current index: {index}")

    def text_changed(self, text):
        print(text)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
