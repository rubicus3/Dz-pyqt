import sys

from PyQt6 import QtWidgets

from window import Ui_Form


class MainWindow(QtWidgets.QWidget, Ui_Form):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.setupUi(self)

        self.btnClear.clicked.connect(self.clear_input)
        self.btnSave.clicked.connect(self.save_file)
        self.btnQuit.clicked.connect(self.quit_app)

    def clear_input(self):
        self.textEdit.clear()

    def save_file(self):
        with open("1.txt", "w") as f:
            f.write(self.textEdit.toPlainText())

    def quit_app(self):
        QtWidgets.QApplication.quit()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()

    window.show()
    app.exec()
