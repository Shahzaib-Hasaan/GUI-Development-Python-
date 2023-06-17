import numpy as np
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 690)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.path = QtWidgets.QLineEdit(self.centralwidget)
        self.path.setGeometry(QtCore.QRect(110, 15, 113, 25))
        self.path.setObjectName("path")
        self.browse = QtWidgets.QPushButton(self.centralwidget)
        self.browse.setGeometry(QtCore.QRect(280, 15, 80, 25))
        self.browse.setObjectName("browse")
        self.flipup = QtWidgets.QPushButton(self.centralwidget)
        self.flipup.setGeometry(QtCore.QRect(120, 60, 80, 25))
        self.flipup.setObjectName("flipup")
        self.fliplr = QtWidgets.QPushButton(self.centralwidget)
        self.fliplr.setGeometry(QtCore.QRect(250, 60, 80, 25))
        self.fliplr.setObjectName("fliplr")
        self.rotate90_ = QtWidgets.QPushButton(self.centralwidget)
        self.rotate90_.setGeometry(QtCore.QRect(380, 60, 80, 25))
        self.rotate90_.setObjectName("rotate90")
        self.filter3 = QtWidgets.QPushButton(self.centralwidget)
        self.filter3.setGeometry(QtCore.QRect(380, 90, 80, 25))
        self.filter3.setObjectName("filter3")
        self.filter1 = QtWidgets.QPushButton(self.centralwidget)
        self.filter1.setGeometry(QtCore.QRect(120, 90, 80, 25))
        self.filter1.setObjectName("filter1")
        self.filter2 = QtWidgets.QPushButton(self.centralwidget)
        self.filter2.setGeometry(QtCore.QRect(250, 90, 80, 25))
        self.filter2.setObjectName("filter2")
        self.imageshow = QtWidgets.QLabel(self.centralwidget)
        self.imageshow.setGeometry(QtCore.QRect(5, 120, 790, 515))
        self.imageshow.setScaledContents(True)  # Scale the pixmap to fit the label
        self.imageshow.setObjectName("imageshow")
        self.imageshow.setText("Image")
        self.close = QtWidgets.QPushButton(self.centralwidget)
        self.close.setGeometry(QtCore.QRect(40, 645, 80, 25))
        self.close.setObjectName("close")
        self.save = QtWidgets.QPushButton(self.centralwidget)
        self.save.setGeometry(QtCore.QRect(540, 645, 80, 25))
        self.save.setObjectName("save")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.browse.clicked.connect(self.show_image)
        self.fliplr.clicked.connect(self.lr_image)
        self.flipup.clicked.connect(self.flip_up)
        self.filter1.clicked.connect(self.apply_filter1)
        self.filter2.clicked.connect(self.apply_filter2)
        self.filter3.clicked.connect(self.apply_filter3)
        self.rotate90_.clicked.connect(self.rotate90)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Filter App"))
        self.browse.setText(_translate("MainWindow", "Browse"))
        self.rotate90_.setText(_translate("MainWindow", "Rotate Left"))
        self.fliplr.setText(_translate("MainWindow", "Flip LR"))
        self.flipup.setText(_translate("MainWindow", "Flip UP"))
        self.filter3.setText(_translate("MainWindow", "Filter 3"))
        self.filter1.setText(_translate("MainWindow", "Filter 1"))
        self.filter2.setText(_translate("MainWindow", "Filter 2"))
        self.close.setText(_translate("MainWindow", "Close"))
        self.save.setText(_translate("MainWindow", "Save"))

    def show_image(self):
        image_path = self.path.text()
        pixmap = QPixmap(image_path)
        self.current_pixmap = pixmap.scaled(self.imageshow.size(), QtCore.Qt.KeepAspectRatio)
        self.imageshow.setPixmap(self.current_pixmap)

    def lr_image(self):
        image_path = self.path.text()
        pixmap = QPixmap(image_path)
        image = pixmap.toImage()

        # Convert QImage to numpy array
        width = image.width()
        height = image.height()
        buffer = image.bits().asstring(width * height * 4)
        image_np = np.frombuffer(buffer, dtype=np.uint8).reshape((height, width, 4))

        flipped_image = np.fliplr(image_np)

        # Convert numpy array back to QImage
        flipped_qimage = QtGui.QImage(flipped_image.tobytes(), flipped_image.shape[1], flipped_image.shape[0], QtGui.QImage.Format_RGBA8888)

        # Convert QImage to QPixmap
        flipped_pixmap = QPixmap.fromImage(flipped_qimage)
        self.current_pixmap = flipped_pixmap.scaled(self.imageshow.size(), QtCore.Qt.KeepAspectRatio)
        self.imageshow.setPixmap(self.current_pixmap)

    def flip_up(self):
        image_path = self.path.text()
        pixmap = QPixmap(image_path)
        image = pixmap.toImage()

        # Convert QImage to numpy array
        width = image.width()
        height = image.height()
        buffer = image.bits().asstring(width * height * 4)
        image_np = np.frombuffer(buffer, dtype=np.uint8).reshape((height, width, 4))

        if image_np.ndim == 2:  # Grayscale image
            rotated_image = np.rot90(image_np, k=1)
        elif image_np.ndim == 3:  # Color image
            rotated_image = np.rot90(image_np, k=1, axes=(1, 0))
        else:
            # Handle unsupported image format
            return

        rotated_image = np.transpose(rotated_image, (1, 0, 2))

        # Convert numpy array back to QImage
        rotated_qimage = QtGui.QImage(rotated_image.data.tobytes(), rotated_image.shape[1], rotated_image.shape[0], QtGui.QImage.Format_RGBA8888)

        # Convert QImage to QPixmap
        rotated_pixmap = QPixmap.fromImage(rotated_qimage)
        self.current_pixmap = rotated_pixmap.scaled(self.imageshow.size(), QtCore.Qt.KeepAspectRatio)
        self.imageshow.setPixmap(self.current_pixmap)

    def apply_filter1(self):
        image_path = self.path.text()
        pixmap = QPixmap(image_path)
        image = pixmap.toImage()

        # Convert QImage to numpy array
        width = image.width()
        height = image.height()
        buffer = image.bits().asstring(width * height * 4)
        image_np = np.frombuffer(buffer, dtype=np.uint8).reshape((height, width, 4))

        # Apply filter 1 to the image (example: increase blue channel values)
        filtered_image = image_np.copy()
        filtered_image[:, :, 2] = filtered_image[:, :, 2] * 0.4
        # filtered_image[:, :, 1] = filtered_image[:, :, 1] * 0.8

        # Clip pixel values to the valid range (0-255)
        filtered_image = np.clip(filtered_image, 0, 255)

        # Convert numpy array back to QImage
        filtered_qimage = QtGui.QImage(filtered_image.data.tobytes(), filtered_image.shape[1], filtered_image.shape[0], QtGui.QImage.Format_RGBA8888)

        # Convert QImage to QPixmap
        filtered_pixmap = QPixmap.fromImage(filtered_qimage)
        self.current_pixmap = filtered_pixmap.scaled(self.imageshow.size(), QtCore.Qt.KeepAspectRatio)
        self.imageshow.setPixmap(self.current_pixmap)
    def apply_filter2(self):
        image_path = self.path.text()
        pixmap = QPixmap(image_path)
        image = pixmap.toImage()

        # Convert QImage to numpy array
        width = image.width()
        height = image.height()
        buffer = image.bits().asstring(width * height * 4)
        image_np = np.frombuffer(buffer, dtype=np.uint8).reshape((height, width, 4))

        # Apply filter 1 to the image (example: increase saturation and contrast)
        filtered_image = image_np.copy()

        # Increase saturation (multiply the RGB channels)
        filtered_image[:, :, 0] = filtered_image[:, :, 0] * 0.3  # Increase red channel
        filtered_image[:, :, 1] = filtered_image[:, :, 1] * 0.6  # Increase green channel
        filtered_image[:, :, 2] = filtered_image[:, :, 2] * 0.8  # Decrease blue channel

        # Increase contrast (subtract/add a constant value to RGB channels)
        filtered_image[:, :, 0] = np.clip(filtered_image[:, :, 0] +1, 0, 255)  # Decrease red channel
        filtered_image[:, :, 1] = np.clip(filtered_image[:, :, 1] + 10, 0, 255)  # Increase green channel
        filtered_image[:, :, 2] = np.clip(filtered_image[:, :, 2] + 5, 0, 255)  # Increase blue channel

        # Convert numpy array back to QImage
        filtered_qimage = QtGui.QImage(filtered_image.data.tobytes(), filtered_image.shape[1], filtered_image.shape[0], QtGui.QImage.Format_RGBA8888)

        # Convert QImage to QPixmap
        filtered_pixmap = QPixmap.fromImage(filtered_qimage)
        self.current_pixmap = filtered_pixmap.scaled(self.imageshow.size(), QtCore.Qt.KeepAspectRatio)
        self.imageshow.setPixmap(self.current_pixmap)

    def apply_filter3(self):
        image_path = self.path.text()
        pixmap = QPixmap(image_path)
        image = pixmap.toImage()

        # Convert QImage to numpy array
        width = image.width()
        height = image.height()
        buffer = image.bits().asstring(width * height * 4)
        image_np = np.frombuffer(buffer, dtype=np.uint8).reshape((height, width, 4))

        # Apply filter 1 to the image (example: enhance colors and contrast)
        filtered_image = image_np.copy()
        # Changing the color of the image to give a different look
        filtered_image[:, :, 0] = np.clip(filtered_image[:, :, 0] + 5, 100, 255)  # Increase red channel
        filtered_image[:, :, 1] = np.clip(filtered_image[:, :, 1] + 5, 39, 255)  # Increase green channel
        filtered_image[:, :, 2] = np.clip(filtered_image[:, :, 2] + 5, 10, 255)  # Increase blue channel

        # Increase contrast (multiply the RGB channels by a constant value)
        filtered_image[:, :, 0] = np.clip(filtered_image[:, :, 0] * 1.2, 0, 255)  # Increase red channel
        filtered_image[:, :, 1] = np.clip(filtered_image[:, :, 1] * 1.2, 0, 255)  # Increase green channel
        filtered_image[:, :, 2] = np.clip(filtered_image[:, :, 2] * 1.2, 0, 255)  # Increase blue channel

        

        # Convert numpy array back to QImage
        filtered_qimage = QtGui.QImage(filtered_image.data.tobytes(), filtered_image.shape[1], filtered_image.shape[0], QtGui.QImage.Format_RGBA8888)

        # Convert QImage to QPixmap
        filtered_pixmap = QPixmap.fromImage(filtered_qimage)
        self.current_pixmap = filtered_pixmap.scaled(self.imageshow.size(), QtCore.Qt.KeepAspectRatio)
        self.imageshow.setPixmap(self.current_pixmap)


    def rotate90(self):
        image_path = self.path.text()
        pixmap = QPixmap(image_path)
        image = pixmap.toImage()

        # Convert QImage to numpy array
        width = image.width()
        height = image.height()
        buffer = image.bits().asstring(width * height * 4)
        image_np = np.frombuffer(buffer, dtype=np.uint8).reshape((height, width, 4))

        # Apply filter 3 to the image
        filtered_image = np.rot90(image_np, k=1)

        # Convert numpy array back to QImage
        filtered_qimage = QtGui.QImage(filtered_image.data.tobytes(), filtered_image.shape[1], filtered_image.shape[0], QtGui.QImage.Format_RGBA8888)

        # Convert QImage to QPixmap
        filtered_pixmap = QPixmap.fromImage(filtered_qimage)
        self.current_pixmap = filtered_pixmap.scaled(self.imageshow.size(), QtCore.Qt.KeepAspectRatio)
        self.imageshow.setPixmap(self.current_pixmap)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
        # Set background colors for buttons
    ui.browse.setStyleSheet("background-color: #4287f5;")
    ui.flipup.setStyleSheet("background-color: #42f55f;")
    ui.fliplr.setStyleSheet("background-color: #f54242;")
    ui.filter1.setStyleSheet("background-color: #f5e542;")
    ui.filter2.setStyleSheet("background-color: #42f5f2;")
    ui.filter3.setStyleSheet("background-color: #d342f5;")
    ui.close.setStyleSheet("background-color: #f5428f;")
    ui.save.setStyleSheet("background-color: #42a1f5;")
    ui.rotate90_.setStyleSheet("background-color: #f5a142;")
    MainWindow.show()
    sys.exit(app.exec_())