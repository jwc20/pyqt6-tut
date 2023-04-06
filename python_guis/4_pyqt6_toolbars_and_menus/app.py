import sys

from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QToolBar, QStatusBar
from PyQt6.QtGui import QIcon, QAction
from PyQt6.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("My App")
        self.setGeometry(400, 400, 400, 400)


app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec()
