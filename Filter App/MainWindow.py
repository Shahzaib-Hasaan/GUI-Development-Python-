from PySide6 import QtCore, QtGui, QtWidgets
from PIL import Image
from FilterApp_ui1 import Ui_MainWindow

class MainWindow(Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Filter App")
        self.toolButton.clicked.connect(self.select_photo)
        self.pushButton.clicked.connect(self.image_show)
        self.flipup.clicked.connect(self.flip_up)
        self.fliplr.clicked.connect(self.flip_horizontal)
        self.rotate90.clicked.connect(self.rotate_90_degrees)
        self.frame.setSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        self.setFixedSize(self.size())
        self.num_flips = 0
        self.horizontal_flipped = False  # Track the current state of horizontal flip
        self.rotation_angle = 0  # Track the current rotation angle

    def flip_up(self):
        image_path = self.path.text()
        if image_path:
            image = Image.open(image_path)
            flipped_image = image.transpose(
                Image.FLIP_TOP_BOTTOM if self.num_flips % 2 == 0 else Image.FLIP_LEFT_RIGHT
            )
            self.num_flips += 1
            self.display_image(flipped_image)
        else:
            self.show_error_message("Please enter a photo")

    def select_photo(self):
        photo_path, _ = QtWidgets.QFileDialog.getOpenFileName(
            self, "Select Photo", "", "Image Files (*.png *.jpg *.jpeg)"
        )
        if photo_path:
            self.path.setText(photo_path)

    def image_show(self):
        image_path = self.path.text()
        if image_path:
            image = Image.open(image_path)
            self.num_flips = 0  # Reset the number of flips when displaying a new image
            self.horizontal_flipped = False  # Reset the horizontal flip state
            self.rotation_angle = 0  # Reset the rotation angle
            self.display_image(image)
        else:
            self.show_error_message("Please enter a photo")

    def display_image(self, image):
        if image.mode != "RGBA":
            new_image = Image.new("RGBA", image.size)
            new_image.paste(image, (0, 0))
            image = new_image
        image.thumbnail((self.imageshow.width(), self.imageshow.height()), Image.ANTIALIAS)
        pixmap = QtGui.QPixmap.fromImage(
            QtGui.QImage(
                image.tobytes("raw", "RGBA"),
                image.size[0],
                image.size[1],
                QtGui.QImage.Format_RGBA8888,
            )
        )
        self.imageshow.clear()
        self.imageshow.setPixmap(pixmap)
        self.imageshow.setAlignment(QtCore.Qt.AlignCenter)
        self.imageshow.setScaledContents(True)
        self.imageshow.setSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding
        )
        self.imageshow.adjustSize()
        self.frame_2.layout().addWidget(self.imageshow)
        self.frame_2.adjustSize()
        self.adjustSize()

    def show_error_message(self, message):
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle("Error")
        msg.setText(message)
        msg.setIcon(QtWidgets.QMessageBox.Critical)
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)
        msg.setDefaultButton(QtWidgets.QMessageBox.Cancel)
        msg.setInformativeText("Photo is required")
        msg.exec_()

    def flip_horizontal(self):
        image_path = self.path.text()
        if image_path:
            image = Image.open(image_path)
            flipped_image = image.transpose(Image.FLIP_LEFT_RIGHT)
            self.horizontal_flipped = not self.horizontal_flipped  # Toggle horizontal flip state
            if self.horizontal_flipped:
                self.display_image(flipped_image)
            else:
                self.display_image(image)
        else:
            self.show_error_message("Please enter a photo")

    def rotate_90_degrees(self):
        image_path = self.path.text()
        if image_path:
            image = Image.open(image_path)
            rotated_image = image.rotate(90 * (self.rotation_angle % 4))
            self.rotation_angle += 1
            self.display_image(rotated_image)
        else:
            self.show_error_message("Please enter a photo")


def main():
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()


if __name__ == "__main__":
    main()
