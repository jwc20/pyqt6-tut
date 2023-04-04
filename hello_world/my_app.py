# Needed for access to command line arguments.
import sys 

from PyQt6.QtCore import Qt, QSize
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton


# Subclass QMainWindow to customize your application's main window.
class MainWindow(QMainWindow): 
    def __init__(self): 
        # Call the constructor of the parent class. (QMainWindow) to set up the main window.
        super().__init__() 
        self.setWindowTitle("My App") 
        button = QPushButton("Press Me!") 

        # Set the fixed size of the window. 
        self.setFixedSize(QSize(400, 300))

        # Set the central widget of the main window to be the button.
        self.setCentralWidget(button) 


# Create the application object. Need only one QApplication object per application. 
# sys.argv is a list of command line arguments. 
app = QApplication(sys.argv) 

# Create a window object. Need only one QWidget object per window.
window = MainWindow()

# Show the window. 
window.show() 

# Start the event loop. 
app.exec() 

