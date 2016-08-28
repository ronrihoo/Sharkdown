import os
import sys
from PyQt4.QtGui import *

from constants import AppConstants
import GUI.sharkdown_ui as sharkdown_ui


class MainWindow(QMainWindow, sharkdown_ui.Ui_Sharkdown):
    def __init__(self):
        QMainWindow.__init__(self)
        QMainWindow.setWindowTitle(self, AppConstants.data['properties']['title'])
        self.setupUi(self)
        # MENU - FILE
        self.actionNew.setText(AppConstants.data['actions']['new'])
        self.actionLoad.setText(AppConstants.data['actions']['load'])
        self.actionSave.setText(AppConstants.data['actions']['save'])
        self.actionSave_As.setText(AppConstants.data['actions']['save_as'])
        self.actionExit.setText(AppConstants.data['actions']['exit'])
        self.actionNew.triggered.connect(self.new_file)
        self.actionLoad.triggered.connect(self.load_file)
        self.actionSave.triggered.connect(self.save_file)
        self.actionSave_As.triggered.connect(self.save_as_file)
        self.actionExit.triggered.connect(self.exit_program)
        # MENU - VIEW
        self.actionEditor_Viewer.setText(AppConstants.data['actions']['editor_viewer'])
        self.actionEditor_Only.setText(AppConstants.data['actions']['editor_only'])
        self.actionViewer_Only.setText(AppConstants.data['actions']['viewer_only'])
        self.actionEditor_Viewer.triggered.connect(self.split_view)
        self.actionEditor_Only.triggered.connect(self.editor_only)
        self.actionViewer_Only.triggered.connect(self.viewer_only)
        # MENU - HELP
        self.actionDocs.setText(AppConstants.data['actions']['docs'])
        self.actionAbout.setText(AppConstants.data['actions']['about'])
        self.actionDocs.triggered.connect(self.send_to_docs)
        self.actionAbout.triggered.connect(self.about_popup)
        # MAIN FUNCTIONALITY
        self.Markdown.setText("This or the Apocalypse")  # initial text for testing
        self.Markdown.textChanged.connect(self.parse_and_convert)
        self.show()
        # CYCLE-SUPPORT (ERROR-CHECKING)
        # ...

    def parse_and_convert(self):
        plain = self.Markdown.toPlainText()
        # ... parse... convert... return
        self.HtmlViewer.setHtml(plain)
        print(plain)  # to see unformatted text (for testing)

    def new_file(self):
        self.Markdown.setText('')

    def load_file(self):
        filedialog = QFileDialog()
        try:
            filename = QFileDialog.getOpenFileName(filedialog, 'Open File', os.path.expanduser('~'),
                                                   "Markdown (*.md, *.markdown); Text (*.txt)")
            with open(filename, 'r') as f:
                self.Markdown.setText('')
                self.Markdown.insertPlainText(f.read())
        except:
            print("'Load' operation closed.")
            pass

    def save_file(self):
        pass

    def save_as_file(self):
        filedialog = QFileDialog()
        filename = QFileDialog.getSaveFileName(filedialog, 'Save As...', os.path.expanduser('~'),
                                               "Markdown (*.md, *.markdown); Text (*.txt)")
        if filename:
            print(filename)
            with open(filename, 'w') as file:
                file.write(str(self.Markdown.toPlainText()))
        else:
            print("'Save As' operation closed.")

    def exit_program(self):
        # make modal via dialog box--if work is unsaved. But for now, just close. // diff
        self.close()

    def split_view(self):
        self.Markdown.setVisible(True)
        self.HtmlViewer.setVisible(True)

    def editor_only(self):
        self.Markdown.setVisible(True)
        self.HtmlViewer.setVisible(False)

    def viewer_only(self):
        self.Markdown.setVisible(False)
        self.HtmlViewer.setVisible(True)

    def send_to_docs(self):
        pass

    def about_popup(self):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    app.exec_()
