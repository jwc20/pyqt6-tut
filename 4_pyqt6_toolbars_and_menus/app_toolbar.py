import sys

from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QToolBar, QStatusBar
from PyQt6.QtGui import QIcon, QAction
from PyQt6.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("Toolbar")
        self.setGeometry(400, 400, 400, 400)

        label = QLabel("Hello World")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.setCentralWidget(label)

        toolbar = QToolBar("My main toolbar")
        self.addToolBar(toolbar)

    def onMyToolBarButtonClick(self, s):
        print("click", s)


app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec()
