"""
https://www.pythonguis.com/tutorials/pyside6-plotting-pyqtgraph/
Plotting with PyQtGraph
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
        self.graphWidget.setTitle("Your Title Here", color="b", size="30pt")
        styles = {"color": "#F00", "font-size": "20px"}
        self.graphWidget.setLabel("left", "Temperature (°C)", **styles)
        self.graphWidget.setLabel("bottom", "Hour (H)", **styles)

        self.graphWidget.addLegend(offset=(50, 50))
        self.graphWidget.showGrid(x=True, y=True)

        self.setCentralWidget(self.graphWidget)

        hour = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        temperature = [30, 32, 34, 32, 33, 31, 29, 32, 35, 45]

        color = self.palette().color(QtGui.QPalette.ColorRole.Window)
        self.graphWidget.setBackground(color)
        self.graphWidget.setXRange(0, 11, padding=0)
        self.graphWidget.setYRange(20, 55, padding=0)
        # self.graphWidget.setBackground(QtGui.QColor(100, 50, 254, 25))
        pen = pg.mkPen(color=(255, 0, 0), width=5, style=pg.QtCore.Qt.DashLine)
        self.graphWidget.plot(
            hour,
            temperature,
            name="Sensor 1",
            pen=pen,
            symbol="+",
            symbolSize=30,
            symbolBrush=("b"),
        )


app = QApplication(sys.argv)
main = MainWindow()
main.show()
app.exec()
