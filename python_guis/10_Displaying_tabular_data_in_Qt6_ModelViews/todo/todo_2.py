import sys

from PyQt6 import QtCore, QtGui, QtWidgets, uic
from PyQt6.QtCore import Qt, QAbstractListModel


qt_creator_file = "mainwindow.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qt_creator_file)


class TodoModel(QtCore.QAbstractListModel):
    def __init__(self, todos=None):
        super().__init__()
        # self.todos = todos or []
        self.model = TodoModel(todos)
        self.todoView.setModel(self.model)

        # Connect the button 
        self.addButton.pressed.connect(self.add)


    def data(self, index, role):
        """
        This function is called by the view to get the data to display.
        """
        if role == Qt.ItemDataRole.DisplayRole:
            status, text = self.todo[index.row()]
            return text


    def rowCount(self, index):
        """
        This function is called by the view to get the number of rows.
        """
        return len(self.todos)


    def add(self): 
        """ 
        Add an item to our todo list, getting the text from the QLineEdit .todoEdit and then clearing it.
        """
        text = self.todoEdit.text() 

        # Remove whitespace from the ends of the string. 
        text = text.strip() 
        if text: # If the string is not empty 
            self.model.todos.append((False, text))
            self.model.layoutChanged.emit()  # Emit a signal to tell the view that the model has changed.
            self.todoEdit.setText("")


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        # todos = [(False, "Buy milk"), (True, "Buy eggs"), (False, "Buy bread")]
        # model = TodoModel(todos)
        self.setupUi(self)
        # self.todoView.setModel(self.model)


app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
