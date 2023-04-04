import sys
from PyQt6.QtWidgets import (
    QMainWindow,
    QApplication,
    QLabel,
    QCheckBox,
    QComboBox,
    QListWidget,
    QLineEdit,
    QLineEdit,
    QSpinBox,
    QDoubleSpinBox,
    QSlider,
)
from PyQt6.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("My App")

        widget = QLabel("Hello")
        font = widget.font()
        font.setPointSize(28)
        widget.setFont(font)
        widget.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # you can also set the image
        # widget,setPixmap(QPixmap("icon.png"))
        # widget.setScaledContents(True)

        self.setCentralWidget(widget)


app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()
