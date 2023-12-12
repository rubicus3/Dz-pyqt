import sys

from PyQt6 import QtWidgets

from window import Ui_Form


class MainWindow(QtWidgets.QWidget, Ui_Form):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.setupUi(self)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()

    window.show()
    app.exec()
