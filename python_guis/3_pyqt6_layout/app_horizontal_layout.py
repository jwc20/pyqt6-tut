import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout
from PyQt6.QtGui import QPalette, QColor


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")
        self.setGeometry(400, 400, 400, 400)

        layout = QHBoxLayout() 

        layout.addWidget(Color('red')) 
        layout.addWidget(Color('green'))
        layout.addWidget(Color('blue')) 

        widget = QWidget()
        widget.setLayout(layout) 
        self.setCentralWidget(widget)
        


class Color(QWidget): 
    def __init__(self, color):
        super(Color, self).__init__()
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor(color))
        self.setPalette(palette) 


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
