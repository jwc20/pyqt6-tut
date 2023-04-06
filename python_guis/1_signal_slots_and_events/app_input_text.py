from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QVBoxLayout, QMainWindow
 

import sys 


class MainWindow(QMainWindow): 
    def __init__(self): 
        super().__init__() 

        self.setWindowTitle("My App") 

        self.label = QLabel() 

        self.input = QLineEdit() 
        self.input.textChanged.connect(self.label.setText)

        layout = QVBoxLayout() 
        layout.addWidget(self.input) 
        layout.addWidget(self.label) 

        container = QWidget() 
        container.setLayout(layout) 

        self.setCentralWidget(container)


app = QApplication(sys.argv) 

window = MainWindow()
window.show()

app.exec()

