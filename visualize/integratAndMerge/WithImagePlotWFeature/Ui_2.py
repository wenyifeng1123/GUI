# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_2.ui'
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
        self.matplotlibwidget_static.setGeometry(QtCore.QRect(480, 30, 601, 681))
        self.matplotlibwidget_static.setObjectName("matplotlibwidget_static")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 100, 191, 311))
        self.groupBox.setObjectName("groupBox")
        self.wyShowArchitecture = QtWidgets.QPushButton(self.groupBox)
        self.wyShowArchitecture.setGeometry(QtCore.QRect(20, 20, 151, 21))
        self.wyShowArchitecture.setObjectName("wyShowArchitecture")
        self.radioButton = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton.setGeometry(QtCore.QRect(50, 60, 71, 16))
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_2.setGeometry(QtCore.QRect(50, 80, 71, 16))
        self.radioButton_2.setObjectName("radioButton_2")
        self.listView = QtWidgets.QListView(self.groupBox)
        self.listView.setGeometry(QtCore.QRect(20, 100, 151, 171))
        self.listView.setObjectName("listView")
        self.wyPlot = QtWidgets.QPushButton(self.groupBox)
        self.wyPlot.setGeometry(QtCore.QRect(20, 280, 151, 23))
        self.wyPlot.setObjectName("wyPlot")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 30, 191, 51))
        self.groupBox_3.setObjectName("groupBox_3")
        self.wyChooseFile = QtWidgets.QPushButton(self.groupBox_3)
        self.wyChooseFile.setGeometry(QtCore.QRect(20, 20, 151, 23))
        self.wyChooseFile.setObjectName("wyChooseFile")
        self.groupBox_5 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_5.setGeometry(QtCore.QRect(10, 420, 191, 51))
        self.groupBox_5.setObjectName("groupBox_5")
        self.wySubsetSelection = QtWidgets.QPushButton(self.groupBox_5)
        self.wySubsetSelection.setGeometry(QtCore.QRect(20, 20, 151, 23))
        self.wySubsetSelection.setObjectName("wySubsetSelection")
        self.matplotlibwidget_static_2 = MatplotlibWidget(self.centralwidget)
        self.matplotlibwidget_static_2.setGeometry(QtCore.QRect(270, 20, 741, 571))
        self.matplotlibwidget_static_2.setObjectName("matplotlibwidget_static_2")
        self.horizontalSlider = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider.setGeometry(QtCore.QRect(480, 720, 521, 22))
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.lcdNumber = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber.setGeometry(QtCore.QRect(1010, 720, 71, 23))
        self.lcdNumber.setObjectName("lcdNumber")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(210, 10, 241, 701))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 239, 699))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
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
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "Visualization of Architecture"))
        self.wyShowArchitecture.setText(_translate("MainWindow", "Show the Weights"))
        self.radioButton.setText(_translate("MainWindow", "Weights"))
        self.radioButton_2.setText(_translate("MainWindow", "Features"))
        self.wyPlot.setText(_translate("MainWindow", "Plot"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Choose one H5 file"))
        self.wyChooseFile.setText(_translate("MainWindow", "Choose the file"))
        self.groupBox_5.setTitle(_translate("MainWindow", "DeepVisualization"))
        self.wySubsetSelection.setText(_translate("MainWindow", "Show Subset Selection"))

from test import MatplotlibWidget
