"""
https://www.pythonguis.com/tutorials/pyside6-qtableview-modelviews-numpy-pandas/
Display tabular data in Qt ModelViews
"""
import sys
import typing
from datetime import datetime

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

    def data(
        self, index: typing.Union[QtCore.QModelIndex, QtCore.QPersistentModelIndex], role=...
    ) -> typing.Any:
        if role == Qt.ItemDataRole.DisplayRole:
            # See below for the nested-list data structure.
            # .row() indexes into the outer list,
            # .column() indexes into the sub-list
            value = self._data[index.row()][index.column()]
            if isinstance(value, datetime):
                return value.strftime("%Y-%m-%d")
            if isinstance(value, float):
                return "%.2f" % value
            if isinstance(value, str):
                return '"%s"' % value
            return value
        if role == Qt.ItemDataRole.TextAlignmentRole:
            value = self._data[index.row()][index.column()]
            if isinstance(value, int) or isinstance(value, float):
                return Qt.AlignmentFlag.AlignCenter + Qt.AlignmentFlag.AlignRight
            else:
                return Qt.AlignmentFlag.AlignJustify
        if role == Qt.ItemDataRole.ForegroundRole:
            value = self._data[index.row()][index.column()]

            if (isinstance(value, int) or isinstance(value, float)) and value < 0:
                return QtGui.QColor("red")
        if role == Qt.ItemDataRole.DecorationRole:
            value = self._data[index.row()][index.column()]
            if isinstance(value, bool):
                if value:
                    return QtGui.QIcon('tick.png')
                return QtGui.QIcon('cross.png')
            if isinstance(value, int) or isinstance(value, float):
                value = int(value)  # Convert to integer for indexing.
                # Limit to range -5 ... +5, then convert to 0..10
                value = max(-5, value)  # values < -5 become -5
                value = min(5, value)  # valaues > +5 become +5
                value = value + 5  # -5 becomes 0, +5 becomes + 10
                return QtGui.QColor(COLORS[value])

            if isinstance(value, datetime):
                return QtGui.QIcon("calendar.png")

    def rowCount(self, index):
        return len(self._data)

    def columnCount(self, index):
        # The following takes the first sub-list, and returns
        # the length (only works if all rows are an equal length)
        return len(self._data[0])


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.setBaseSize(QSize(300, 300))
        self.setMinimumSize(QSize(400, 250))

        self.table = QtWidgets.QTableView()
        data = [
            [True, 9, 2],
            [1, -1, "hello"],
            [3.023, 5, False],
            [3, 3, datetime(2017, 10, 1)],
            [7.555, 8, 9],
        ]

        self.model = TableModel(data)
        self.table.setModel(self.model)

        self.setCentralWidget(self.table)


app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
