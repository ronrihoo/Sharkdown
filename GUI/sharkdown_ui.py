# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sharkdown.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Sharkdown(object):
    def setupUi(self, Sharkdown):
        Sharkdown.setObjectName(_fromUtf8("Sharkdown"))
        Sharkdown.resize(800, 600)
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.NoAntialias)
        Sharkdown.setFont(font)
        self.centralwidget = QtGui.QWidget(Sharkdown)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.horizontal_layout = QtGui.QHBoxLayout()
        self.horizontal_layout.setObjectName(_fromUtf8("horizontal_layout"))
        self.Markdown = QtGui.QTextEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("MS Sans Serif"))
        font.setPointSize(12)
        font.setKerning(False)
        self.Markdown.setFont(font)
        self.Markdown.setMouseTracking(True)
        self.Markdown.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.Markdown.setObjectName(_fromUtf8("Markdown"))
        self.horizontal_layout.addWidget(self.Markdown)
        self.HtmlViewer = QtGui.QTextBrowser(self.centralwidget)
        self.HtmlViewer.setObjectName(_fromUtf8("HtmlViewer"))
        self.horizontal_layout.addWidget(self.HtmlViewer)
        self.horizontalLayout.addLayout(self.horizontal_layout)
        Sharkdown.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(Sharkdown)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuView = QtGui.QMenu(self.menubar)
        self.menuView.setObjectName(_fromUtf8("menuView"))
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        Sharkdown.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(Sharkdown)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        Sharkdown.setStatusBar(self.statusbar)
        self.actionEditor_Viewer = QtGui.QAction(Sharkdown)
        self.actionEditor_Viewer.setObjectName(_fromUtf8("actionEditor_Viewer"))
        self.actionEditor_Only = QtGui.QAction(Sharkdown)
        self.actionEditor_Only.setObjectName(_fromUtf8("actionEditor_Only"))
        self.actionViewer_Only = QtGui.QAction(Sharkdown)
        self.actionViewer_Only.setObjectName(_fromUtf8("actionViewer_Only"))
        self.actionNew = QtGui.QAction(Sharkdown)
        self.actionNew.setObjectName(_fromUtf8("actionNew"))
        self.actionSave = QtGui.QAction(Sharkdown)
        self.actionSave.setObjectName(_fromUtf8("actionSave"))
        self.actionSave_As = QtGui.QAction(Sharkdown)
        self.actionSave_As.setObjectName(_fromUtf8("actionSave_As"))
        self.actionClose = QtGui.QAction(Sharkdown)
        self.actionClose.setObjectName(_fromUtf8("actionClose"))
        self.actionExit = QtGui.QAction(Sharkdown)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.actionDocs = QtGui.QAction(Sharkdown)
        self.actionDocs.setObjectName(_fromUtf8("actionDocs"))
        self.actionAbout = QtGui.QAction(Sharkdown)
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
        self.actionLoad = QtGui.QAction(Sharkdown)
        self.actionLoad.setObjectName(_fromUtf8("actionLoad"))
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionLoad)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSave_As)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuView.addAction(self.actionEditor_Viewer)
        self.menuView.addAction(self.actionEditor_Only)
        self.menuView.addAction(self.actionViewer_Only)
        self.menuHelp.addAction(self.actionDocs)
        self.menuHelp.addSeparator()
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(Sharkdown)
        QtCore.QMetaObject.connectSlotsByName(Sharkdown)

    def retranslateUi(self, Sharkdown):
        Sharkdown.setWindowTitle(_translate("Sharkdown", "Sharkdown", None))
        self.menuFile.setTitle(_translate("Sharkdown", "File", None))
        self.menuView.setTitle(_translate("Sharkdown", "View", None))
        self.menuHelp.setTitle(_translate("Sharkdown", "Help", None))
        self.actionEditor_Viewer.setText(_translate("Sharkdown", "Editor - Viewer", None))
        self.actionEditor_Viewer.setShortcut(_translate("Sharkdown", "Alt+1", None))
        self.actionEditor_Only.setText(_translate("Sharkdown", "Editor Only", None))
        self.actionEditor_Only.setShortcut(_translate("Sharkdown", "Alt+2", None))
        self.actionViewer_Only.setText(_translate("Sharkdown", "Viewer Only", None))
        self.actionViewer_Only.setShortcut(_translate("Sharkdown", "Alt+3", None))
        self.actionNew.setText(_translate("Sharkdown", "New", None))
        self.actionNew.setShortcut(_translate("Sharkdown", "Ctrl+N", None))
        self.actionSave.setText(_translate("Sharkdown", "Save", None))
        self.actionSave.setShortcut(_translate("Sharkdown", "Ctrl+S", None))
        self.actionSave_As.setText(_translate("Sharkdown", "Save As", None))
        self.actionSave_As.setShortcut(_translate("Sharkdown", "Ctrl+Shift+S", None))
        self.actionClose.setText(_translate("Sharkdown", "Close", None))
        self.actionExit.setText(_translate("Sharkdown", "Exit", None))
        self.actionExit.setShortcut(_translate("Sharkdown", "Ctrl+Q", None))
        self.actionDocs.setText(_translate("Sharkdown", "Docs", None))
        self.actionAbout.setText(_translate("Sharkdown", "About", None))
        self.actionLoad.setText(_translate("Sharkdown", "Load", None))

