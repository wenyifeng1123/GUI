# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_matplotlib_pyqt_scroll.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1088, 800)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.matplotlibwidget_static = MatplotlibWidget(self.centralwidget)
        self.matplotlibwidget_static.setGeometry(QtCore.QRect(399, 10, 301, 700))
        self.matplotlibwidget_static.setObjectName("matplotlibwidget_static")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 30, 101, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 240, 101, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(190, 10, 881, 531))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1000, 1000))
        self.scrollAreaWidgetContents.setMinimumSize(QtCore.QSize(1000, 1000))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.matplotlibwidget_static_2 = MatplotlibWidget(self.scrollAreaWidgetContents)
        self.matplotlibwidget_static_2.setGeometry(QtCore.QRect(10, 10, 831, 491))
        self.matplotlibwidget_static_2.setObjectName("matplotlibwidget_static_2")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1088, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pushButton.clicked.connect(self.matplotlibwidget_static.show)
        self.pushButton_2.clicked.connect(self.matplotlibwidget_static_2.show)
        self.pushButton.clicked.connect(self.matplotlibwidget_static_2.hide)
        self.pushButton_2.clicked.connect(self.matplotlibwidget_static.hide)
        self.pushButton.clicked.connect(self.scrollArea.hide)
        self.pushButton_2.clicked.connect(self.scrollArea.show)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "weights"))
        self.pushButton_2.setText(_translate("MainWindow", "archietecture"))

from matplotlibwidget import MatplotlibWidget
