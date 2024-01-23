"""
https://www.pythonguis.com/tutorials/multithreading-pyside6-applications-qthreadpool/
Multithreading application with QThreadPool
"""
import sys
import time
from PySide6.QtWidgets import QApplication, QLabel, QMainWindow, QPushButton, QVBoxLayout, QWidget
from PySide6.QtCore import QTimer


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.counter = 0

        layout = QVBoxLayout()

        self.label = QLabel("Start")
        button = QPushButton("DANGER!")
        button.pressed.connect(self.oh_no)

        layout.addWidget(self.label)
        layout.addWidget(button)

        widget = QWidget()
        widget.setLayout(layout)

        self.setCentralWidget(widget)

        self.show()

        self.timer = QTimer()
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.recurring_timer)
        self.timer.start()

    def oh_no(self):
        time.sleep(5)

    def recurring_timer(self):
        self.counter += 1
        self.label.setText("Counter: %d" % self.counter)


app = QApplication(sys.argv)
window = MainWindow()
app.exec()
