"""
Lesson 3
https://www.pythonguis.com/tutorials/pyside6-widgets/
Виджеты
QSlider
"""
import sys

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QSlider,
                               QVBoxLayout, QWidget)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QSlider App")

        layout = QVBoxLayout()

        self.label_hslider = QLabel("Vertical slider: 0")

        self.hslider = QSlider()
        font = self.hslider.font()
        font.setPointSize(30)
        self.hslider.setFont(font)
        self.hslider.setStyleSheet("color: blue")
        self.hslider.setRange(0, 40)
        self.hslider.setSingleStep(2)
        self.hslider.setTickInterval(5)
        self.hslider.setTickPosition(QSlider.TickPosition.TicksRight)

        self.hslider.valueChanged.connect(self.value_changed)
        self.hslider.sliderMoved.connect(self.slider_position)
        self.hslider.sliderPressed.connect(self.slider_pressed)
        self.hslider.sliderReleased.connect(self.slider_released)

        self.setCentralWidget(self.hslider)

        self.label = QLabel("Horisontal slider: 0")
        self.g_slider = QSlider(Qt.Orientation.Horizontal)
        self.g_slider.setMinimum(-10)
        self.g_slider.setMaximum(10)
        self.g_slider.setTickInterval(2)
        self.g_slider.setTickPosition(QSlider.TickPosition.TicksAbove)
        self.g_slider.valueChanged.connect(self.value_changed_g)

        layout.addWidget(self.label_hslider)
        layout.addWidget(self.hslider)
        layout.addWidget(self.label)
        layout.addWidget(self.g_slider)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def value_changed(self, value):
        print("Value changed ...")
        self.label_hslider.setText("Vertical slider: " + str(value))

    def value_changed_g(self, value):
        print("Value changed ...")
        self.label.setText("Horisontal slider: "+str(value))

    def slider_pressed(self):
        print("Pressed")

    def slider_position(self, position):
        print(f"Position {position}")

    def slider_released(self):
        print("Released")


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
