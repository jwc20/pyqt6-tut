import sys 
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton 


class MainWindow(QMainWindow): 
    def __init__(self): 
        super().__init__() 
        self.setWindowTitle("My App") 

app = QApplication(sys.argv) 
window = MainWindow() 

window.show()
 
app.exec()
