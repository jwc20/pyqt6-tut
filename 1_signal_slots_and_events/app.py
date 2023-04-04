from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton

import sys
from random import choice


# Define a list of possible window titles. 
window_titles = [
    "My App",
    "My App",
    "Still My App",
    "Still My App",
    "What on earth",
    "What on earth",
    "This is surprising",
    "This is surprising",
    "Something went wrong",
]


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.n_times_clicked = 0

        self.setWindowTitle("My App")

        self.button = QPushButton("Press Me!")

        # Connect the button's "clicked" signal to the "the_button_was_clicked" slot.
        self.button.clicked.connect(self.the_button_was_clicked)

        # Connect the window's "windowTitleChanged" signal to the "the_window_title_changed" slot.
        self.windowTitleChanged.connect(self.the_window_title_changed)

        # Set the central widget of the Window.
        self.setCentralWidget(self.button)

    def the_button_was_clicked(self):
        print("Clicked.")
        new_window_title = choice(window_titles)
        print("Setting title:  %s" % new_window_title)
        self.setWindowTitle(new_window_title)


    # Define a method to be called when the window title is changed.
    def the_window_title_changed(self, window_title):
        print("Window title changed: %s" % window_title)

        # Disable the button if the window title is "Something went wrong".
        if window_title == "Something went wrong":
            self.button.setDisabled(True)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
