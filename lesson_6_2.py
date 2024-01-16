"""
https://www.pythonguis.com/tutorials/pyside6-dialogs/
Dialogs
"""
import sys

from PySide6.QtCore import QSize
from PySide6.QtWidgets import (QApplication, QDialog, QDialogButtonBox, QLabel,
                               QMainWindow, QPushButton, QVBoxLayout)


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

        dlg = CustomDialog(self)
        if dlg.exec():
            print("Success!")
        else:
            print("Cancel!")


class CustomDialog(QDialog):
    """
    Custom Dialog with my widgets.
    If parent != None Dialog shows in MainWindow,
    else Dialog shows in centre Screen.
    """

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("HELLO!")
        self.setMinimumSize(200, 200)

        buttons = QDialogButtonBox.StandardButton.Ok
        buttons |= QDialogButtonBox.StandardButton.Cancel
        self.buttonBox = QDialogButtonBox(buttons)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        layout = QVBoxLayout()
        message = QLabel("Something happened, is that OK?")
        layout.addWidget(message)
        layout.addWidget(self.buttonBox)
        self.setLayout(layout)


app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec()
