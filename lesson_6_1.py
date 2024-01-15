"""
https://www.pythonguis.com/tutorials/pyside6-dialogs/
Dialogs
"""
import sys

from PySide6.QtCore import QSize
from PySide6.QtWidgets import QApplication, QDialog, QMainWindow, QPushButton


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Dialogs")
        self.setMinimumSize(QSize(400, 300))

        button = QPushButton("Press me for a dialog!")
        button.clicked.connect(self.button_clicked)
        self.setCentralWidget(button)

    def button_clicked(self, s):
        print("Click", s)

        dlg = QDialog(self)
        dlg.setMinimumSize(200, 200)
        dlg.setWindowTitle("HELLO!")
        dlg.exec()


app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec()
