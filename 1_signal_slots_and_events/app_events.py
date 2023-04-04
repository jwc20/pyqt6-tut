import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QTextEdit


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.label = QLabel("Click in this window")
        self.setCentralWidget(self.label)

    def mouseMoveEvent(self, event):
        self.label.setText(f"Mouse at {event.pos()}")

    def mousePressEvent(self, event):
        self.label.setText(f"Mouse pressed at {event.pos()}")

    def mouseReleaseEvent(self, event):
        self.label.setText(f"Mouse released at {event.pos()}")

    def mouseDoubleClickEvent(self, event):
        self.label.setText(f"Mouse double clicked at {event.pos()}")


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
