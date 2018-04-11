# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui.ui'
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
        self.matplotlibwidget_static.setGeometry(QtCore.QRect(210, 0, 181, 731))
        self.matplotlibwidget_static.setObjectName("matplotlibwidget_static")
        self.matplotlibwidget_static_2 = MatplotlibWidget(self.centralwidget)
        self.matplotlibwidget_static_2.setGeometry(QtCore.QRect(480, 30, 601, 681))
        self.matplotlibwidget_static_2.setObjectName("matplotlibwidget_static_2")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 100, 191, 51))
        self.groupBox.setObjectName("groupBox")
        self.wy2 = QtWidgets.QPushButton(self.groupBox)
        self.wy2.setGeometry(QtCore.QRect(20, 20, 151, 21))
        self.wy2.setObjectName("wy2")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 30, 191, 51))
        self.groupBox_3.setObjectName("groupBox_3")
        self.wy1 = QtWidgets.QPushButton(self.groupBox_3)
        self.wy1.setGeometry(QtCore.QRect(20, 20, 151, 23))
        self.wy1.setObjectName("wy1")
        self.groupBox_5 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_5.setGeometry(QtCore.QRect(10, 160, 191, 51))
        self.groupBox_5.setObjectName("groupBox_5")
        self.wy3 = QtWidgets.QPushButton(self.groupBox_5)
        self.wy3.setGeometry(QtCore.QRect(20, 20, 151, 23))
        self.wy3.setObjectName("wy3")
        self.matplotlibwidget_static_3 = MatplotlibWidget(self.centralwidget)
        self.matplotlibwidget_static_3.setGeometry(QtCore.QRect(270, 20, 741, 571))
        self.matplotlibwidget_static_3.setObjectName("matplotlibwidget_static_3")
        self.horizontalSlider = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider.setGeometry(QtCore.QRect(480, 720, 521, 22))
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.lcdNumber = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber.setGeometry(QtCore.QRect(1010, 720, 71, 23))
        self.lcdNumber.setObjectName("lcdNumber")
        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setGeometry(QtCore.QRect(400, 100, 71, 16))
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_2.setGeometry(QtCore.QRect(400, 150, 71, 16))
        self.radioButton_2.setObjectName("radioButton_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1088, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "Visualization of Architecture"))
        self.wy2.setText(_translate("MainWindow", "Show the Weights"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Choose one H5 file"))
        self.wy1.setText(_translate("MainWindow", "Choose the file"))
        self.groupBox_5.setTitle(_translate("MainWindow", "DeepVisualization"))
        self.wy3.setText(_translate("MainWindow", "Show Subset Selection"))
        self.radioButton.setText(_translate("MainWindow", "Weights"))
        self.radioButton_2.setText(_translate("MainWindow", "Features"))

from test import MatplotlibWidget
