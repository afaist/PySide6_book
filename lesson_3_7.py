"""
Lesson 3
https://www.pythonguis.com/tutorials/pyside6-widgets/
Виджеты
Qself.lineedit
"""
import sys

from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
                               QVBoxLayout, QWidget)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QLineEdit App")

        layout = QVBoxLayout()

        self.lineedit = QLineEdit()
        font = self.lineedit.font()
        font.setPointSize(30)
        self.lineedit.setFont(font)
        self.lineedit.setStyleSheet("color: blue")

        self.lineedit.returnPressed.connect(self.return_pressed)
        self.lineedit.selectionChanged.connect(self.selection_changed)
        self.lineedit.textChanged.connect(self.text_changed)
        self.lineedit.textEdited.connect(self.text_edited)
        self.setCentralWidget(self.lineedit)

        self.label = QLabel("Input IP:")
        self.ipedit = QLineEdit()
        self.ipedit.setInputMask("000.000.000.000;_")

        layout.addWidget(self.lineedit)
        layout.addWidget(self.label)
        layout.addWidget(self.ipedit)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def return_pressed(self):
        print("Return pressed!")
        self.lineedit.setText("BOOM!")

    def selection_changed(self):
        print("Selection changed")
        print(self.lineedit.selectedText())

    def text_edited(self, text):
        print("Text edited...")
        print(text)

    def text_changed(self, text):
        print("Text changed...")
        print(text)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
