import sys
from PyQt4.QtGui import *

from constants import AppConstants
import GUI.sharkdown_ui as sharkdown_ui


class MainWindow(QMainWindow, sharkdown_ui.Ui_Sharkdown):
    def __init__(self):
        QMainWindow.__init__(self)
        QMainWindow.setWindowTitle(self, AppConstants.data['properties']['title'])
        self.setupUi(self)
        self.actionNew.triggered.connect(self.new_file)
        self.actionLoad.triggered.connect(self.load_file)
        self.actionSave.triggered.connect(self.save_file)
        self.actionSave_As.triggered.connect(self.save_as_file)
        self.actionExit.triggered.connect(self.exit_program)
        self.Markdown.setText("This or the Apocalypse")             # initial text for testing
        self.Markdown.textChanged.connect(self.parse_and_convert)
        self.show()

    def parse_and_convert(self):
        plain = self.Markdown.toPlainText()
        self.HtmlViewer.setHtml(plain)
        print(plain)            # to see unformatted text

    def new_file(self):
        self.Markdown.setText('')

    def load_file(self):
        widget = QFileDialog()
        try:
            filename = QFileDialog.getOpenFileName(widget, 'Open File', '/')
            self.Markdown.setText('')
            with open(filename, 'r') as f:
                self.Markdown.insertPlainText(f.read())
        except:
            # we'll do something later
            pass

    def save_file(self):
        pass

    def save_as_file(self):
        pass

    def exit_program(self):
        # make modal via dialog box--if work is unsaved. But for now, just close.
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    app.exec_()