"""
https://www.pythonguis.com/tutorials/pyside6-qtableview-modelviews-numpy-pandas/
Table with pandas
"""
import sys

import pandas as pd
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import QSize, Qt

COLORS = [
    "#053061",
    "#2166ac",
    "#4393c3",
    "#92c5de",
    "#d1e5f0",
    "#f7f7f7",
    "#fddbc7",
    "#f4a582",
    "#d6604d",
    "#b2182b",
    "#67001f",
]


class TableModel(QtCore.QAbstractTableModel):
    def __init__(self, data):
        super(TableModel, self).__init__()
        self._data = data

    def data(self, index, role):
        value = self._data.iloc[index.row(), index.column()]
        if role == Qt.ItemDataRole.DisplayRole:
            return str(value)
        if role == Qt.ItemDataRole.TextAlignmentRole:
            if pd.api.types.is_number(value):
                return Qt.AlignmentFlag.AlignRight
            else:
                return Qt.AlignmentFlag.AlignCenter
        if role == Qt.ItemDataRole.ForegroundRole:
            if pd.api.types.is_number(value):
                if value < 0:
                    return QtGui.QColor("red")
                return QtGui.QColor("yellow")
        if role == Qt.ItemDataRole.BackgroundRole:
            if pd.api.types.is_number(value):
                color_index = int(value)
                color_index = max(-5, color_index)
                color_index = min(5, color_index)
                color_index = color_index + 5
                return QtGui.QColor(COLORS[color_index])

    def rowCount(self, index):
        return self._data.shape[0]

    def columnCount(self, index):
        return self._data.shape[1]

    def headerData(self, section, orientation, role):
        # section is the index of the column/row.
        if role == Qt.ItemDataRole.DisplayRole:
            if orientation == Qt.Orientation.Horizontal:
                return str(self._data.columns[section])

            if orientation == Qt.Orientation.Vertical:
                return str(self._data.index[section])


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.setMinimumSize(QSize(400, 300))
        self.table = QtWidgets.QTableView()

        data = pd.DataFrame(
            [
                [1, 9.3, 2],
                [1, 0, -1],
                [3, -5, 2],
                [3, 3, 2],
                [5, 8, 9],
            ],
            columns=["A", "B", "C"],
            index=["Row 1", "Row 2", "Row 3", "Row 4", "Row 5"],
        )

        self.model = TableModel(data)
        self.table.setModel(self.model)

        self.setCentralWidget(self.table)


app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
