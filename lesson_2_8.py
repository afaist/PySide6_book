"""
Lesson 2
https://www.pythonguis.com/tutorials/pyside6-signals-slots-events/
Mouse events
События мыши
"""
# Only needed for access to command line arguments
import sys

from PySide6 import QtGui
from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import QApplication, QLabel, QMainWindow


# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Мое приложение")

        self.label = QLabel("Click in the window")

        self.setMinimumSize(QSize(400, 300))
        self.setCentralWidget(self.label)

    def mouseMoveEvent(self, event: QtGui.QMouseEvent) -> None:
        self.label.setText("mouseMoveEvent")

    def mousePressEvent(self, event: QtGui.QMouseEvent) -> None:
        if event.button() == Qt.MouseButton.LeftButton:
            self.label.setText("mousePressEvent LeftButton")
        elif event.button() == Qt.MouseButton.MiddleButton:
            self.label.setText("mousePressEvent MiddleButton")
        elif event.button() == Qt.MouseButton.RightButton:
            self.label.setText("mousePressEvent RightButton")

    def mouseDoubleClickEvent(self, event: QtGui.QMouseEvent) -> None:
        if event.button() == Qt.MouseButton.LeftButton:
            self.label.setText("mouseDoubleClickEvent LeftButton")
        elif event.button() == Qt.MouseButton.MiddleButton:
            self.label.setText("mouseDoubleClickEvent MiddleButton")
        elif event.button() == Qt.MouseButton.RightButton:
            self.label.setText("mouseDoubleClickEvent RightButton")

    def mouseReleaseEvent(self, event: QtGui.QMouseEvent) -> None:
        if event.button() == Qt.MouseButton.LeftButton:
            self.label.setText("mouseReleaseEvent LeftButton")
        elif event.button() == Qt.MouseButton.MiddleButton:
            self.label.setText("mouseReleaseEvent MiddleButton")
        elif event.button() == Qt.MouseButton.RightButton:
            self.label.setText("mouseReleaseEvent RightButton")


# You need one (and only one) QApplication isinstance per application.
# Pass in sys.argv to allow command line arguments for your app.
# If you know yow won't use command line arguments QApplication([]) works too.
app = QApplication(sys.argv)
# Create a Qt widget, which will be our window.
window = MainWindow()
window.show()  # IMPORTANT!!! Windows are hidden by default.
# Start the event loop.
app.exec()
