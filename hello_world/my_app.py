from PyQt6.QtWidgets import QApplication, QWidget 

# Needed for access to command line arguments.
import sys 

# Create the application object. Need only one QApplication object per application. 
# sys.argv is a list of command line arguments. 
app = QApplication(sys.argv) 

# Create a window object. Need only one QWidget object per window.
window = QWidget()


# Show the window. 
window.show() 

# Start the event loop. 
app.exec() 

