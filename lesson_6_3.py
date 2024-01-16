"""
https://www.pythonguis.com/tutorials/pyside6-dialogs/
Dialogs
"""
import sys

from PySide6.QtCore import QSize
from PySide6.QtWidgets import (QApplication, QMainWindow, QMessageBox,
                               QPushButton)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Dialogs")
        self.setMinimumSize(QSize(400, 300))

        button = QPushButton("Press me for a dialog!")
        button.clicked.connect(self.button_clicked)
        self.setCentralWidget(button)

    def button_clicked(self, s):
        dlg = QMessageBox(self)
        dlg.setWindowTitle("I have a question!")
        dlg.setText("This is a simple dialog")
        dlg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        dlg.setIcon(QMessageBox.Question)
        button = dlg.exec()
        if button == QMessageBox.Yes:
            print("Yes!")
        else:
            print("No!")


app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec()
