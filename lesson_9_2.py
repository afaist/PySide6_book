"""
https://www.pythonguis.com/tutorials/pyside6-plotting-pyqtgraph/
Plotting with PyQtGraph
Plotting multiple lines
"""
import sys

from PySide6 import QtGui
from PySide6.QtWidgets import QApplication, QMainWindow
# Important import pyqtgraph AFTER PySide6
import pyqtgraph as pg


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.graphWidget = pg.PlotWidget()
        self.setCentralWidget(self.graphWidget)

        hour = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        temperature_1 = [30, 32, 34, 32, 33, 31, 29, 32, 35, 45]
        temperature_2 = [50, 35, 44, 22, 38, 32, 27, 38, 32, 44]

        self.graphWidget.setTitle("Your Title Here", color="b", size="30pt")
        styles = {"color": "#F00", "font-size": "20px"}
        self.graphWidget.setLabel("left", "Temperature (°C)", **styles)
        self.graphWidget.setLabel("bottom", "Hour (H)", **styles)

        self.graphWidget.addLegend()
        self.graphWidget.showGrid(x=True, y=True)

        color = self.palette().color(QtGui.QPalette.ColorRole.Window)
        self.graphWidget.setBackground(color)
        self.graphWidget.setXRange(0, 11, padding=0)
        self.graphWidget.setYRange(20, 55, padding=0)
        self.plot(hour, temperature_1, "Sensor1", "r")
        self.plot(hour, temperature_2, "Sensor2", "b")

    def plot(self, x, y, plotname, color):
        pen = pg.mkPen(color=color)
        self.graphWidget.plot(
            x, y, name=plotname, pen=pen, symbol="+", symbolSize=30, symbolBrush=(color)
        )


app = QApplication(sys.argv)
main = MainWindow()
main.show()
app.exec()
