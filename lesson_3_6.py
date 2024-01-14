"""
Lesson 3
https://www.pythonguis.com/tutorials/pyside6-widgets/
Виджеты
QListWidget
"""
import sys

from PySide6.QtWidgets import QApplication, QListWidget, QMainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Qlistwidget App")

        listwidget = QListWidget()
        font = listwidget.font()
        font.setPointSize(30)
        listwidget.setFont(font)
        listwidget.setStyleSheet("color: blue")
        listwidget.addItems(["One", "Two", "Three", "Four"])

        listwidget.currentItemChanged.connect(self.index_changed)
        listwidget.currentTextChanged.connect(self.text_changed)

        self.setCentralWidget(listwidget)

    def text_changed(self, text):
        print(text)

    def index_changed(self, index):
        print(index.text())


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
