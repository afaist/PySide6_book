# This Python file uses the following encoding: utf-8
import sys
import json
from TodoModel import TodoModel

from PyQt6.QtWidgets import QApplication
from PyQt6 import QtGui, QtWidgets, uic, QtCore

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
qt_creator_file = "mainwindow.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qt_creator_file)
tick = QtGui.QImage('tick.png')


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.model = TodoModel()
        self.load()
        self.todoView.setModel(self.model)
        self.addButton.pressed.connect(self.add)
        self.deleteButton.pressed.connect(self.delete)
        self.completeButton.pressed.connect(self.complete)
        self.setAttribute(QtCore.Qt.WidgetAttribute.WA_DeleteOnClose)

    def add(self):
        """
        Add an item to our todo list, getting the text from the QLineEdit .todoEdit
        and then clearing it.
        """
        text = self.todoEdit.text()
        if text: # Don't add empty strings.
            # Access the list via the model.
            self.model.todos.append((False, text))
            # Trigger refresh.
            self.model.layoutChanged.emit()
            # Empty the input
            self.todoEdit.setText("")
            self.save()

    def delete(self):
        indexes = self.todoView.selectedIndexes()
        if indexes:
            # Indexes is a list of a single item in single-select mode.
            index = indexes[0]
            # Remove the item and refresh.
            del self.model.todos[index.row()]
            self.model.layoutChanged.emit()
            # Clear the selection (as it is no longer valid).
            self.todoView.clearSelection()
            self.save()

    def complete(self):
        indexes = self.todoView.selectedIndexes()
        if indexes:
            index = indexes[0]
            row = index.row()
            status, text = self.model.todos[row]
            self.model.todos[row] = (True, text)
            # .dataChanged takes top-left and bottom right, which are equal
            # for a single selection.
            self.model.dataChanged.emit(index, index)
            # Clear the selection (as it is no longer valid).
            self.todoView.clearSelection()
            self.save()

    def load(self):
        try:
            with open('data.db', 'r') as f:
                self.model.todos = json.load(f)
        except Exception:
            pass

    def save(self):
        with open('data.db', 'w') as f:
            json.dump(self.model.todos, f)




if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
