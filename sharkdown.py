import os
import sys
from PyQt4.QtGui import *

from sdparser import sharkdownparser as parser
from util.constants import AppConstants
import gui.sharkdownui as sharkdownui
import gui.uiconfig as uiconfig

# TODO: autoscroll for both editor and viewer widgets


class MainWindow(QMainWindow, sharkdownui.Ui_Sharkdown):
    def __init__(self):
        QMainWindow.__init__(self)

        # FILE STORAGE
        self.filepath = "-1"
        self.filename = "-1"
        self.fullpath = ""
        self.temp_path_storage = ""

        # CURSOR
        self.cursor_code = 0

        # APP UI
        self.setupUi(self)
        self.set_window_title()
        uiconfig.setup(self)

        # MAIN FUNCTIONALITY
        self.Markdown.textChanged.connect(self.parse_and_convert)
        self.show()

        # CYCLE-SUPPORT (+ERROR-CHECKING)
        # ...
        # TODO: implement diff notification (compare against last saved state)...

    # PARSING AND CONVERSION

    # TODO: get diff; parse; convert; return; modify with precision (important for overall performance, at this state)
    def parse_and_convert(self):
        plain = self.Markdown.toPlainText()
        plain = parser(plain)
        self.HtmlViewer.setHtml(plain)
        print(plain)  # TESTING: to see unformatted text (for testing)

    # WINDOW MANAGEMENT

    # TODO: adapt window title to diff implementation
    def set_window_title(self):
        if self.filename != "-1":
            QMainWindow.setWindowTitle(self, AppConstants.data['properties']['title'] + " - " + self.filename)
        else:
            QMainWindow.setWindowTitle(self, AppConstants.data['properties']['title'] + " - new*")

    # PATH MANAGEMENT

    def decide_path(self):
        self.backup_path()
        self.filepath = os.getcwd() if self.filepath == "-1" else self.filepath

    def learn_path(self, fullpath):
        self.filepath, self.filename = os.path.split(fullpath)

    def backup_path(self):
        self.temp_path_storage = self.fullpath

    def restore_path(self):
        self.fullpath = self.temp_path_storage

    # TEXT CURSOR

    def get_cursor(self):
        return self.Markdown.textCursor()

    def get_cursor_pos(self):
        return self.get_cursor().position()

    def get_selected_range(self):
        cursor = self.get_cursor()
        return cursor.selectionStart(), cursor.selectionEnd()

    def set_cursor_back(self, index_substraction):
        cursor = self.Markdown.textCursor()
        cursor.setPosition(self.get_cursor_pos() - index_substraction)
        self.Markdown.setTextCursor(cursor)

    def set_cursor_forward(self, index_addition):
        cursor = self.Markdown.textCursor()
        cursor.setPosition(self.get_cursor_pos() + index_addition)
        self.Markdown.setTextCursor(cursor)

    # MENU - FILE

    # TODO: does not show (*.md, *.markdown) files when opening and saving (in Windows 7) -- fix and check other OS

    def new_file(self):
        self.Markdown.setText('')
        self.filename = "-1"
        self.fullpath = ""
        self.set_window_title()
        # WARNING: do not reset filepath; it's used for staying in the last given directory

    def load_file(self):
        filedialog = QFileDialog()
        try:
            self.decide_path()
            self.fullpath = QFileDialog.getOpenFileName(filedialog, 'Open File', self.filepath,
                                                        "Markdown (*.md, *.markdown); Text (*.txt)")
            with open(self.fullpath, 'r') as f:
                self.Markdown.setText('')
                self.Markdown.insertPlainText(f.read())
                print(f.read())
                self.learn_path(self.fullpath)
                self.set_window_title()
                print(self.fullpath)
        except:
            self.restore_path()
            print("'Load' operation stopped.")

    def save_file(self):
        print(self.fullpath)
        if self.fullpath != "":
            with open(self.fullpath, 'w') as file:
                file.write(str(self.Markdown.toPlainText()))
                self.set_window_title()
                print("Finished saving file.")
        else:
            self.save_as_file()

    def save_as_file(self):
        filedialog = QFileDialog()
        self.decide_path()
        self.fullpath = QFileDialog.getSaveFileName(filedialog, 'Save As...', self.filepath,
                                                    "Markdown (*.md, *.markdown); Text (*.txt)")
        if self.fullpath:
            with open(self.fullpath, 'w') as file:
                self.learn_path(self.fullpath)
                file.write(str(self.Markdown.toPlainText()))
                self.set_window_title()
        else:
            self.restore_path()
            print("'Save As' operation stopped.")

    # TODO: implement an exit dialog box
    def exit_program(self):
        # TODO: make modal via dialog box -- for when work is unsaved. But for now, just close.
        # TODO: needs diff implementation (to compare current state to last saved state)
        if self.filename == "" or self.filename == "-1":
            self.close()
        else:
            self.close()
            # it's not all that embarrassing in the mean time...

    # MENU - EDIT

    # Skip Action
    #
    # The heart of the UX lays in this feature -- the more featured-filled, the sweeter.
    #
    # Brief: after auto-inserting MD code, your cursor goes in the ready position (e.g., in the middle) for that code,
    #        and you can press Alt+Enter to skip forward through the code once done typing content within it; therefore,
    #        never leaving the keyboard.
    def skip_action(self):
        self.set_cursor_forward(AppConstants.data['cursor_skip'][self.cursor_code])
        self.cursor_code = 'default'

    # MENU - VIEW

    def split_view(self):
        self.Markdown.setVisible(True)
        self.HtmlViewer.setVisible(True)

    def editor_only(self):
        self.Markdown.setVisible(True)
        self.HtmlViewer.setVisible(False)

    def viewer_only(self):
        self.Markdown.setVisible(False)
        self.HtmlViewer.setVisible(True)

    # MENU - FORMAT - FUNCTIONS

    def h1_action(self):
        self.Markdown.insertPlainText(AppConstants.style['layout']['h1'])
        self.cursor_code = AppConstants.data['cursor_code']['h1']

    def h2_action(self):
        self.Markdown.insertPlainText(AppConstants.style['layout']['h2'])
        self.cursor_code = AppConstants.data['cursor_code']['h2']

    def h3_action(self):
        self.Markdown.insertPlainText(AppConstants.style['layout']['h3'])
        self.cursor_code = AppConstants.data['cursor_code']['h3']

    def bold_action(self):
        self.Markdown.insertPlainText(AppConstants.style['layout']['bold'])
        self.set_cursor_back(AppConstants.data['cursor_back']['bold'])
        self.cursor_code = AppConstants.data['cursor_code']['bold']

    def italic_action(self):
        self.Markdown.insertPlainText(AppConstants.style['layout']['italic'])
        self.set_cursor_back(AppConstants.data['cursor_back']['italic'])
        self.cursor_code = AppConstants.data['cursor_code']['italic']

    def list_action(self):
        self.Markdown.insertPlainText(AppConstants.style['layout']['bullet'])
        self.cursor_code = AppConstants.data['cursor_code']['bullet']

    def inline_code_action(self):
        self.Markdown.insertPlainText(AppConstants.style['layout']['inline_code'])
        self.set_cursor_back(AppConstants.data['cursor_back']['inline_code'])
        self.cursor_code = AppConstants.data['cursor_code']['inline_code']

    def code_block_action(self):
        self.Markdown.insertPlainText(AppConstants.style['layout']['code_block'])
        self.set_cursor_back(AppConstants.data['cursor_back']['code_block'])
        self.cursor_code = AppConstants.data['cursor_code']['code_block']

    def label_code_action(self):
        self.Markdown.insertPlainText(AppConstants.style['layout']['labeled_code'])
        self.set_cursor_back(AppConstants.data['cursor_back']['labeled_code'])
        self.cursor_code = AppConstants.data['cursor_code']['labeled_code']

    def secondary_label_action(self):
        self.Markdown.insertPlainText(AppConstants.style['layout']['secondary_labeled_code'])
        self.set_cursor_back(AppConstants.data['cursor_back']['secondary_labeled_code'])
        self.cursor_code = AppConstants.data['cursor_code']['secondary_labeled_code']

    def variable_action(self):
        self.Markdown.insertPlainText(AppConstants.style['layout']['variable'])
        self.set_cursor_back(AppConstants.data['cursor_back']['variable'])
        self.cursor_code = AppConstants.data['cursor_code']['variable']

    def inline_variable_action(self):
        self.Markdown.insertPlainText(AppConstants.style['layout']['inline_code_variable'])
        self.set_cursor_back(AppConstants.data['cursor_back']['inline_code_variable'])
        self.cursor_code = AppConstants.data['cursor_code']['inline_code_variable']

    def nonroot_action(self):
        self.Markdown.insertPlainText(AppConstants.style['layout']['nonroot_command'])
        self.set_cursor_back(AppConstants.data['cursor_back']['nonroot_command'])
        self.cursor_code = AppConstants.data['cursor_code']['nonroot_command']

    def root_action(self):
        self.Markdown.insertPlainText(AppConstants.style['layout']['root_command'])
        self.set_cursor_back(AppConstants.data['cursor_back']['root_command'])
        self.cursor_code = AppConstants.data['cursor_code']['root_command']

    def custom_action(self):
        self.Markdown.insertPlainText(AppConstants.style['layout']['custom_command'])
        self.set_cursor_back(AppConstants.data['cursor_back']['custom_command'])
        self.cursor_code = AppConstants.data['cursor_code']['custom_command']

    def note_action(self):
        self.Markdown.insertPlainText(AppConstants.style['layout']['note'])
        self.set_cursor_back(AppConstants.data['cursor_back']['note'])
        self.cursor_code = AppConstants.data['cursor_code']['note']

    def warning_action(self):
        self.Markdown.insertPlainText(AppConstants.style['layout']['warning'])
        self.set_cursor_back(AppConstants.data['cursor_back']['warning'])
        self.cursor_code = AppConstants.data['cursor_code']['warning']

    def url_action(self):
        self.Markdown.insertPlainText(AppConstants.style['layout']['url'])
        self.set_cursor_back(AppConstants.data['cursor_back']['url'])
        self.cursor_code = AppConstants.data['cursor_code']['url']

    def image_action(self):
        self.Markdown.insertPlainText(AppConstants.style['layout']['image'])
        self.set_cursor_back(AppConstants.data['cursor_back']['image'])
        self.cursor_code = AppConstants.data['cursor_code']['image']

    def em_dash_action(self):
        self.Markdown.insertPlainText(AppConstants.style['layout']['em_dash'])
        self.cursor_code = AppConstants.data['cursor_code']['em_dash']

    # MENU - HELP

    def send_to_docs(self):
        # TODO: handle this later, since there's no use in writing docs at this point
        pass

    def about_popup(self):
        # TODO: handle this later
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    app.exec_()
