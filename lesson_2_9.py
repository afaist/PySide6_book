"""
Lesson 2
https://www.pythonguis.com/tutorials/pyside6-signals-slots-events/
Context menus
"""
# Only needed for access to command line arguments
import sys

from PySide6.QtCore import QSize
from PySide6.QtGui import QAction
from PySide6.QtWidgets import QApplication, QMainWindow, QMenu


# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Мое приложение")
        self.setMinimumSize(QSize(400, 300))

    def contextMenuEvent(self, event):
        context = QMenu(self)
        context.addAction(QAction("test 1", self))
        context.addAction(QAction("test 2", self))
        context.addAction(QAction("test 3", self))
        context.exec(event.globalPos())


# You need one (and only one) QApplication isinstance per application.
# Pass in sys.argv to allow command line arguments for your app.
# If you know yow won't use command line arguments QApplication([]) works too.
app = QApplication(sys.argv)
# Create a Qt widget, which will be our window.
window = MainWindow()
window.show()  # IMPORTANT!!! Windows are hidden by default.
# Start the event loop.
app.exec()
