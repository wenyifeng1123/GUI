# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_matplotlib_pyqt3.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 800)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.matplotlibwidget_static = MatplotlibWidget(self.centralwidget)
        self.matplotlibwidget_static.setGeometry(QtCore.QRect(490, 10, 210, 700))
        self.matplotlibwidget_static.setObjectName("matplotlibwidget_static")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 30, 101, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 240, 101, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(140, 290, 75, 23))
        self.pushButton_4.setObjectName("pushButton_4")
        self.matplotlibwidget_static_2 = MatplotlibWidget(self.centralwidget)
        self.matplotlibwidget_static_2.setGeometry(QtCore.QRect(260, 30, 881, 701))
        self.matplotlibwidget_static_2.setObjectName("matplotlibwidget_static_2")
        self.horizontalSlider = QtWidgets.QSlider(self.matplotlibwidget_static_2)
        self.horizontalSlider.setGeometry(QtCore.QRect(120, 490, 321, 22))
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(140, 210, 75, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(10, 410, 75, 23))
        self.pushButton_6.setObjectName("pushButton_6")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1000, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pushButton.clicked.connect(self.matplotlibwidget_static.show)
        self.pushButton_2.clicked.connect(self.matplotlibwidget_static_2.show)
        self.pushButton_2.clicked.connect(self.pushButton_4.show)
        self.pushButton.clicked.connect(self.matplotlibwidget_static_2.hide)
        self.pushButton.clicked.connect(self.pushButton_4.hide)
        self.pushButton_2.clicked.connect(self.matplotlibwidget_static.hide)
        self.pushButton.clicked.connect(self.pushButton_3.hide)
        self.pushButton_2.clicked.connect(self.pushButton_3.show)
        self.pushButton_3.clicked.connect(self.openfile)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "weights"))
        self.pushButton_2.setText(_translate("MainWindow", "archietecture"))
        self.pushButton_4.setText(_translate("MainWindow", "predict"))
        self.pushButton_3.setText(_translate("MainWindow", "choose data"))
        self.pushButton_6.setText(_translate("MainWindow", "Deep"))

    def openfile(self):
        openfile_name = QFileDialog.getOpenFileName(self,'Choose the file','','Excel files(*.xlsx , *.xls)')

from MatplotlibWidget import MatplotlibWidget
