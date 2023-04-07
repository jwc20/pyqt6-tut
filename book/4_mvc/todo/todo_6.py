import sys

from PyQt6 import QtCore, QtGui, QtWidgets, uic
from PyQt6.QtCore import Qt, QAbstractListModel

import os
import json

basedir = os.path.dirname(__file__)

tick = QtGui.QImage(os.path.join(basedir, "tick.png"))

qt_creator_file = "mainwindow.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qt_creator_file)


class TodoModel(QtCore.QAbstractListModel):
    def __init__(self, *args, todos=None, **kwargs):
        super(TodoModel, self).__init__(*args, **kwargs)
        self.todos = todos or []

    def data(self, index, role):
        """
        This function is called by the view to get the data to display.
        """
        if role == Qt.ItemDataRole.DisplayRole:
            status, text = self.todos[index.row()]
            return text

        if role == Qt.ItemDataRole.DecorationRole:
            status, text = self.todos[index.row()]
            if status:
                return tick

    def rowCount(self, index):
        """
        This function is called by the view to get the number of rows.
        """
        return len(self.todos)


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.model = TodoModel()
        self.load()
        self.todoView.setModel(self.model)

        # Connect the button
        self.addButton.pressed.connect(self.add)
        self.deleteButton.pressed.connect(self.delete)
        self.completeButton.pressed.connect(self.complete)

    def add(self):
        """
        Add an item to our todo list, getting the text from the QLineEdit .todoEdit and then clearing it.
        """
        text = self.todoEdit.text()

        # Remove whitespace from the ends of the string.
        text = text.strip()
        if text:  # If the string is not empty
            self.model.todos.append((False, text))
            self.model.layoutChanged.emit()  # Emit a signal to tell the view that the model has changed.
            self.todoEdit.setText("")

    def delete(self):
        """
        Delete an item from our todo list, getting the text from the QLineEdit .todoEdit and then clearing it.
        """
        indexes = self.todoView.selectedIndexes()
        if indexes:
            index = indexes[0]
            del self.model.todos[index.row()]
            self.model.layoutChanged.emit()
            self.todoView.clearSelection()

    def complete(self):
        indexes = self.todoView.selectedIndexes()
        if indexes:
            index = indexes[0]
            row = index.row()
            status, text = self.model.todos[row]
            self.model.todos[row] = (True, text)

            self.model.dataChanged.emit(index, index)
            self.todoView.clearSelection()

    def load(self): 
        try: 
            with open('data.db', 'r') as f: 
                self.model.todos = json.load(f)
        except Exception: 
            pass

    def save(self): 
        with open('data.json', 'w') as f: 
            json.dump(self.model.todos, f) 





app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
