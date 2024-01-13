"""
Lesson 2
https://www.pythonguis.com/tutorials/pyside6-signals-slots-events/
Signals, Slots & Events and get Data, storing Data
Изменение заголовока окна по нажатию кнопки
"""
# Only needed for access to command line arguments
import sys
from random import choice

from PySide6.QtCore import QSize
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton

window_titles = [
    "My App",
    "My App",
    "Still My App",
    "Still My App",
    "What on earth",
    "What on earth",
    "This is surprising",
    "This is surprising",
    "Something went wrong",
]


# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.n_times_clicked = 0

        self.setWindowTitle("Мое приложение")

        self.button = QPushButton("Change windows title!")
        self.button.clicked.connect(self.the_button_was_clicked)

        self.windowTitleChanged.connect(self.the_window_title_changed)

        self.setMinimumSize(QSize(400, 300))
        self.setCentralWidget(self.button)

    def the_button_was_clicked(self):
        print("Clicked!")
        new_window_title = choice(window_titles)
        print("Setting title: %s" % new_window_title)
        self.setWindowTitle(new_window_title)

    def the_window_title_changed(self, window_title):
        print("Window title changed: %s" % window_title)
        if window_title == "Something went wrong":
            self.button.setDisabled(True)
            self.button.setText("This is the end!")
            self.button.setStyleSheet(
                "QPushButton {background-color: #A3C1DA; color: red;}"
            )


# You need one (and only one) QApplication isinstance per application.
# Pass in sys.argv to allow command line arguments for your app.
# If you know yow won't use command line arguments QApplication([]) works too.
app = QApplication(sys.argv)
# Create a Qt widget, which will be our window.
window = MainWindow()
window.show()  # IMPORTANT!!! Windows are hidden by default.
# Start the event loop.
app.exec()
