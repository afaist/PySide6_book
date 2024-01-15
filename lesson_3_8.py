"""
Lesson 3
https://www.pythonguis.com/tutorials/pyside6-widgets/
Виджеты
QSpinBox and QDoubleSpinBox
"""
import sys

from PySide6.QtWidgets import (QApplication, QDoubleSpinBox, QLabel,
                               QMainWindow, QSpinBox, QVBoxLayout, QWidget)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QSpinBox App")

        layout = QVBoxLayout()

        label_spin = QLabel("Input integer:")

        self.spinbox = QSpinBox()
        font = self.spinbox.font()
        font.setPointSize(30)
        self.spinbox.setFont(font)
        self.spinbox.setStyleSheet("color: blue")

        self.spinbox.textChanged.connect(self.text_changed)
        self.spinbox.valueChanged.connect(self.value_changed_str)
        self.setCentralWidget(self.spinbox)

        self.label = QLabel("Input float:")
        self.spin_float = QDoubleSpinBox()
        self.spin_float.setMinimum(-1.0)
        self.spin_float.setMaximum(10)

        layout.addWidget(label_spin)
        layout.addWidget(self.spinbox)
        layout.addWidget(self.label)
        layout.addWidget(self.spin_float)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def value_changed_str(self, text):
        print("Value changed ...")
        print(text)

    def text_changed(self, text):
        print("Text changed...")
        print(text)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
