from PySide6 import QtWidgets
import LL_ui as testUI

class MainWindow(testUI.Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.showMaximized()
        self.setWindowTitle("Learning")
        self.populate_tree_widget()
        self.populate_list_widget()
        self.pushButton.clicked.connect(self.fill_form)    
        self.filemenu.clicked.connect(self.select_photo)

    def populate_tree_widget(self):
        self.treeWidget.setHeaderLabels(["Fruit", "Color" , "Size" ,"Price"])
        self.treeWidget.clear()
        x = ["Apple", "Banana", "Orange"]
        y = ["Red", "Yellow", "Orange"]
        z = ["Small", "Medium", "Large"]
        p = ["$1.00", "$1.50", "$2.00"]
        self.treeWidget.setHeaderLabels(["Fruit", "Color" , "Size" ,"Price"])
        for i,j,k,l in zip(x,y,z,p):
            parent = QtWidgets.QTreeWidgetItem(self.treeWidget)
            parent.setText(0, i)
            parent.setText(1, j)
            parent.setText(2, k)
            parent.setText(3, l)

    def populate_list_widget(self):
        self.listWidget.clear()
        x = ["Apple", "Banana", "Orange"]
        y = ["Red", "Yellow", "Orange"]
        z = ["Small", "Medium", "Large"]
        p = ["$1.00", "$1.50", "$2.00"]
        for i,j,k,l in zip(x,y,z,p):
            item = QtWidgets.QListWidgetItem(self.listWidget)
            item.setText(i + " " + j + " " + k + " " + l)

    def fill_form(self):
        name = self.nameinput.text()
        if not name:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle("Error")
            msg.setText("Please enter a name")
            msg.setIcon(QtWidgets.QMessageBox.Critical)
            msg.setStandardButtons(QtWidgets.QMessageBox.Ok|QtWidgets.QMessageBox.Cancel)
            msg.setDefaultButton(QtWidgets.QMessageBox.Cancel)
            msg.setInformativeText("Name is required")
            msg.exec_()
            return
        photo = self.photo.text()
        if not photo:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle("Error")
            msg.setText("Please enter a photo")
            msg.setIcon(QtWidgets.QMessageBox.Critical)
            msg.setStandardButtons(QtWidgets.QMessageBox.Ok|QtWidgets.QMessageBox.Cancel)
            msg.setDefaultButton(QtWidgets.QMessageBox.Cancel)
            msg.setInformativeText("Photo is required")
            msg.exec_()
            return
        
    def select_photo(self):
        photo_path ,ext = QtWidgets.QFileDialog.getOpenFileName(self, "Select Photo", "", "Image Files (*.png *.jpg *.jpeg)")
        if photo_path:
            self.photo.setText(photo_path)
        QtWidgets.QMessageBox.about(self,"Done","Photo Selected")

def main():
    app = QtWidgets.QApplication()
    window = MainWindow()
    window.show()
    app.exec_()
    # return 0

if __name__ == "__main__":
    main()