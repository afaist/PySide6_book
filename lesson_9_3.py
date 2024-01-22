"""
https://www.pythonguis.com/tutorials/pyside6-plotting-pyqtgraph/
Plotting with PyQtGraph
Updating the plot
"""
import sys
from random import randint

from PySide6 import QtGui
from PySide6.QtCore import QTimer
from PySide6.QtWidgets import QApplication, QMainWindow
# Important import pyqtgraph AFTER PySide6
import pyqtgraph as pg


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.graphWidget = pg.PlotWidget()
        self.setCentralWidget(self.graphWidget)

        self.graphWidget.setTitle("Your Title Here", color="b", size="30pt")
        styles = {"color": "#F00", "font-size": "20px"}
        self.graphWidget.setLabel("left", "Temperature (°C)", **styles)
        self.graphWidget.setLabel("bottom", "Seconds (S)", **styles)

        self.graphWidget.showGrid(x=True, y=True)

        color = self.palette().color(QtGui.QPalette.ColorRole.Window)
        self.graphWidget.setBackground(color)
        self.x_data = list(range(100))
        self.y_data = [randint(0, 60) for _ in range(100)]
        pen = pg.mkPen(color=(255, 0, 0))
        self.data_line = self.graphWidget.plot(self.x_data, self.y_data, pen=pen)

        self.timer = QTimer()
        self.timer.setInterval(70)
        self.timer.timeout.connect(self.update_plot_data)
        self.timer.start()

    def update_plot_data(self):
        self.x_data = self.x_data[1:]
        self.x_data.append(self.x_data[-1] + 1)

        self.y_data = self.y_data[1:]
        self.y_data.append(randint(0, 100))

        self.data_line.setData(self.x_data, self.y_data)


app = QApplication(sys.argv)
main = MainWindow()
main.show()
app.exec()
