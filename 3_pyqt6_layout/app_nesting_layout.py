import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout
from PyQt6.QtGui import QPalette, QColor


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")
        self.setGeometry(400, 400, 400, 400)

        layout1 = QHBoxLayout() 
        layout2 = QVBoxLayout() 
        layout3 = QVBoxLayout() 


        layout1.setContentsMargins(0,0,0,0)
        layout1.setSpacing(20)

        layout2.addWidget(Color('red')) 
        layout2.addWidget(Color('green'))
        layout2.addWidget(Color('blue')) 


        layout1.addLayout(layout2)
        layout1.addWidget(Color('yellow')) 

        layout3.addWidget(Color('orange'))
        layout3.addWidget(Color('purple'))

        layout1.addLayout(layout3)

        widget = QWidget()
        widget.setLayout(layout1) 
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
