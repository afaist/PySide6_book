"""
Lesson 1
First application with MainWindow in my class and Button
"""
# Only needed for access to command line arguments
import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton


# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Мое приложение")
        button = QPushButton("Press Me!")
        self.setCentralWidget(button)


# You need one (and only one) QApplication isinstance per application.
# Pass in sys.argv to allow command line arguments for your app.
# If you know yow won't use command line arguments QApplication([]) works too.
app = QApplication(sys.argv)
# Create a Qt widget, which will be our window.
window = MainWindow()
window.show()  # IMPORTANT!!! Windows are hidden by default.
# Start the event loop.
app.exec()
