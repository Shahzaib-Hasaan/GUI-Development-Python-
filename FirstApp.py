from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My First Application")
        self.setGeometry(0, 0, 400, 400)  # x, y, width, height
        self.initUI()

    # On click function for button
    def click(self):
        self.label.setText("I love you, Afnan")

    def initUI(self):
        # Label
        self.label = QtWidgets.QLabel(self)
        self.label.setText("I love Afnan")
        self.label.move(12, 12)  # x, y

        # Button
        self.button = QtWidgets.QPushButton(self)
        self.button.setText("Click me")
        self.button.move(200, 25)

        # On click connect
        self.button.clicked.connect(self.click)

app = QApplication(sys.argv)
win = MyWindow()
win.show()
sys.exit(app.exec_())

