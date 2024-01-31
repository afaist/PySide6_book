"""
https://www-pythonguis-com.translate.goog/tutorials/pyside6-qml-qtquick-python-application/
Create applications with QtQuick
Add signals
"""
import sys
from time import gmtime, localtime, strftime

from PySide6.QtCore import QObject, QTimer, Signal
from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine

strftime("%H:%M:%S", localtime())
strftime("%H:%M:%S", gmtime())

app = QGuiApplication(sys.argv)

engine = QQmlApplicationEngine()
engine.quit.connect(app.quit)
engine.load("main.qml")


class Backend(QObject):
    updated = Signal(str, arguments=["time"])

    def __init__(self):
        super().__init__()

        self.timer = QTimer()
        self.timer.setInterval(100)
        self.timer.timeout.connect(self.update_time)
        self.timer.start()

    def update_time(self):
        # Pass the current time to QML
        curr_time = strftime("%H:%M:%S", localtime())
        engine.rootObjects()[0].setProperty("currTime", curr_time)


backend = Backend()
engine.rootObjects()[0].setProperty("backend", backend)
backend.update_time()

sys.exit(app.exec())
