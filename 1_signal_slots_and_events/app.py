import sys 
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton 


class MainWindow(QMainWindow): 
    def __init__(self): 
        super().__init__() 
        self.setWindowTitle("My App") 

        button = QPushButton("Press Me!") 
        button.setCheckable(True)
        button.clicked.connect(self.the_button_was_clicked) 
        button.toggled.connect(self.the_button_was_toggled)

        # Set the central widget of the Window. 
        self.setCentralWidget(button) 

    # Custom slot
    def the_button_was_clicked(self): 
        print("Clicked!")   

    def the_button_was_toggled(self, checked): 
        print("Checked?", checked) 

app = QApplication(sys.argv) 
window = MainWindow() 

window.show()
 
app.exec()
