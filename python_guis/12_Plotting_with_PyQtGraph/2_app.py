from PyQt6 import QtWidgets, QtGui
import PyQt6.QtCore as QtCore

from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg
import sys  # We need sys so that we can pass argv to QApplication
import os


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.graphWidget = pg.PlotWidget()
        self.setCentralWidget(self.graphWidget)

        hour = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        temperature = [30, 32, 34, 32, 33, 31, 29, 32, 35, 45]

        # Backgraound color
        self.graphWidget.setBackground('w')
        # self.graphWidget.setBackground(QtGui.QColor(100, 50, 254, 25))

        # Line color
        # pen = pg.mkPen(color=(255, 0, 0))
        NewPen = pg.mkPen(
            color=(255, 0, 0), width=2, style=QtCore.Qt.PenStyle.DashDotDotLine
        )

        # Title
        # self.graphWidget.setTitle("<span style=\"color:blue;font-size:30pt\">Your Title Here</span>")
        self.graphWidget.setTitle("Your Title Here", color="b", size="30pt")

        # Axis
        # style = { "color": "#FFF", "font-size": "20px" }
        style = {"color": "r", "font-size": "30pt"}
        self.graphWidget.setLabel("left", "Temperature", **style)
        self.graphWidget.setLabel("bottom", "Hour of Day", **style)


        # Legend
        self.graphWidget.addLegend()

        # Grid 
        self.graphWidget.showGrid(x=True, y=True)

        # Axis Limits 
        self.graphWidget.setXRange(0,11, padding=0) 
        self.graphWidget.setYRange(20, 55, padding=0)

        # Plot
        self.graphWidget.plot(
            hour,
            temperature,
            name="Sensor 1",
            pen=NewPen,
            symbol="+",
            symbolSize=30,
            symbolBrush=("b"),
        )



def main():
    app = QtWidgets.QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
