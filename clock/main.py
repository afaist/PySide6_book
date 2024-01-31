"""
https://www-pythonguis-com.translate.goog/tutorials/pyside6-qml-qtquick-python-application/
Create applications with QtQuick
"""
import sys
from time import gmtime, localtime, strftime

from PySide6.QtCore import QTimer
from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine

strftime("%H:%M:%S", localtime())
strftime("%H:%M:%S", gmtime())

app = QGuiApplication(sys.argv)

engine = QQmlApplicationEngine()
engine.quit.connect(app.quit)
engine.load("main.qml")


def update_time():
    curr_time = strftime("%H:%M:%S", localtime())
    engine.rootObjects()[0].setProperty("currTime", curr_time)


timer = QTimer()
timer.setInterval(100)
timer.timeout.connect(update_time)
timer.start()

update_time()

sys.exit(app.exec())
