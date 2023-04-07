import sys

from PyQt6 import QtCore, QtGui, QtWidgets, uic
from PyQt6.QtCore import Qt, QAbstractListModel


qt_creator_file = "mainwindow.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qt_creator_file)


class TodoModel(QtCore.QAbstractListModel):
    def __init__(self, todos=None):
        super().__init__()
        self.todos = todos or []

    # This function is called by the view to get the data to display
    def data(self, index, role):
        if role == Qt.ItemDataRole.DisplayRole:
            status, text = self.todo[index.row()]
            return text

    # This function is called by the view to get the number of rows
    def rowCount(self, index):
        return len(self.todos)


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        todos = [(False, "Buy milk"), (True, "Buy eggs"), (False, "Buy bread")]
        model = TodoModel(todos)
        self.setupUi(self)
        self.todoView.setModel(self.model)


app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
