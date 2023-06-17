from PySide6.QtCore import Qt
from PySide6.QtGui import QFont, QIcon
from PySide6.QtWidgets import QApplication, QFrame, QGridLayout, QLabel, QLineEdit, QMainWindow, QPushButton, QSizePolicy, QVBoxLayout, QWidget

import icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(847, 637)

        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")

        self.gridLayout_3 = QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)

        self.gridLayout_5 = QGridLayout(self.frame)
        self.gridLayout_5.setObjectName(u"gridLayout_5")

        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(200, 70)
        font = QFont()
        font.setPointSize(20)
        self.label.setFont(font)

        self.imageshow = QLabel(self.frame)
        self.imageshow.setObjectName(u"imageshow")
        self.imageshow.setAutoFillBackground(False)

        self.gridLayout_5.addWidget(self.label, 0, 0, 1, 1)
        self.gridLayout_5.addWidget(self.imageshow, 1, 0, 1, 1)

        self.buttons_layout = QVBoxLayout()
        self.buttons_layout.setSpacing(10)

        self.flipup = QPushButton(self.frame)
        self.flipup.setObjectName(u"flipup")
        self.flipup.setIcon(QIcon(":/Images/down-up.png"))

        self.fliplr = QPushButton(self.frame)
        self.fliplr.setObjectName(u"fliplr")
        self.fliplr.setIcon(QIcon(":/Images/flip1.png"))

        self.rotate90 = QPushButton(self.frame)
        self.rotate90.setObjectName(u"rotate90")
        self.rotate90.setIcon(QIcon(":/Images/rotate-left.png"))

        self.filter1 = QPushButton(self.frame)
        self.filter1.setObjectName(u"filter1")
        self.filter1.setIcon(QIcon(":/Images/filter.png"))

        self.filter2 = QPushButton(self.frame)
        self.filter2.setObjectName(u"filter2")
        self.filter2.setIcon(QIcon(":/Images/adjust.png"))

        self.filter3 = QPushButton(self.frame)
        self.filter3.setObjectName(u"filter3")
        self.filter3.setIcon(QIcon(":/Images/filter1.png"))

        self.buttons_layout.addWidget(self.flipup)
        self.buttons_layout.addWidget(self.fliplr)
        self.buttons_layout.addWidget(self.rotate90)
        self.buttons_layout.addWidget(self.filter1)
        self.buttons_layout.addWidget(self.filter2)
        self.buttons_layout.addWidget(self.filter3)

        self.gridLayout_5.addLayout(self.buttons_layout, 1, 1, 1, 1)

        self.gridLayout_3.addWidget(self.frame, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle("Photo Editor")
        self.label.setText("Select Photo")
        self.flipup.setText("Flip Vertical")
        self.fliplr.setText("Flip Horizontal")
        self.rotate90.setText("Rotate 90")
        self.filter1.setText("Filter 1")
        self.filter2.setText("Filter 2")
        self.filter3.setText("Filter 3")

# # Initialize the application and window
# app = QApplication()
# window = QMainWindow()

# # Create an instance of the UI and set it up
# ui = Ui_MainWindow()
# ui.setupUi(window)

# # Show the window
# window.show()

# # Start the event loop
# app.exec()
