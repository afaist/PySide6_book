"""
Lesson 3
https://www.pythonguis.com/tutorials/pyside6-widgets/
Виджеты
Edit Items in Qself.combobox
"""
import sys

from PySide6.QtWidgets import (QApplication, QComboBox, QMainWindow,
                               QVBoxLayout, QWidget)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Qself.combobox App")

        layout = QVBoxLayout()

        self.combobox = QComboBox()
        font = self.combobox.font()
        font.setPointSize(30)
        self.combobox.setFont(font)
        self.combobox.setStyleSheet("color: blue")
        self.combobox.addItems(["One", "Two", "Three", "Four"])
        self.combobox.setEditable(True)

        self.combobox.currentTextChanged.connect(self.text_changed)

        self.insertpoicy = QComboBox()
        self.insertpoicy.setStyleSheet("color: green")
        self.insertpoicy.addItems(
            [
                "NoInsert",
                "InsertAtTop",
                "InsertAtCurrent",
                "InsertAtBottom",
                "InsertAfterCurrent",
                "InsertBeforeCurrent",
                "InsertAlphabetically",
            ]
        )

        self.insertpoicy.currentIndexChanged.connect(self.change_insert_policy)

        layout.addWidget(self.combobox)
        layout.addWidget(self.insertpoicy)

        central_widget = QWidget()
        central_widget.setLayout(layout)

        self.setCentralWidget(central_widget)

    def text_changed(self, text):
        print(text)

    def change_insert_policy(self, policy):
        self.combobox.setInsertPolicy(QComboBox.InsertPolicy(policy))


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
