import sys

from PyQt4.QtGui import *

import GUI.sharkdown_ui as sharkdown_ui


class MainWindow(QMainWindow, sharkdown_ui.Ui_Sharkdown):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)

        self.Markdown.setText("This or the Apocalypse")

        self.Markdown.textChanged.connect(self.parse_and_convert)
        self.show()

    def parse_and_convert(self):
        plain = self.Markdown.toPlainText()
        self.HtmlViewer.setHtml(plain)
        print(plain)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    app.exec_()