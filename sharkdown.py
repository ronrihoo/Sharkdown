import sys

from PyQt4.QtGui import *
from PyQt4.uic import *

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        ui = loadUi('resources/sharkdown.ui', self)
        ui.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    app.exec_()