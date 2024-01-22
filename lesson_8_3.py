"""
https://www.pythonguis.com/tutorials/pyside6-qtableview-modelviews-numpy-pandas/
Table with numpy
"""
import sys

import numpy as np
from PySide6 import QtCore, QtWidgets
from PySide6.QtCore import QModelIndex, QSize, Qt


class TableModel(QtCore.QAbstractTableModel):
    def __init__(self, data):
        super(TableModel, self).__init__()
        self._data = data

    def data(self, index: QModelIndex, role: Qt.DisplayRole):
        if role == Qt.ItemDataRole.DisplayRole:
            value = self._data[index.row(), index.column()]
            return str(value)

    def rowCount(self, _):
        return self._data.shape[0]

    def columnCount(self, _):
        return self._data.shape[1]


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setMinimumSize(QSize(400, 300))
        self.table = QtWidgets.QTableView()
        self.table.setShowGrid(True)

        data = np.array(
            [
                [1, 9, 2],
                [1, 0, -1],
                [3, 5, 2],
                [3, 3, 2],
                [5, 8, 9],
            ]
        )
        self.model = TableModel(data)
        self.table.setModel(self.model)
        self.setCentralWidget(self.table)


app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
