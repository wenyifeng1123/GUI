# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_3.ui'
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
        self.matplotlibwidget_static.setGeometry(QtCore.QRect(480, 30, 601, 631))
        self.matplotlibwidget_static.setObjectName("matplotlibwidget_static")
        self.matplotlibwidget_static_2 = MatplotlibWidget(self.centralwidget)
        self.matplotlibwidget_static_2.setGeometry(QtCore.QRect(270, 20, 781, 571))
        self.matplotlibwidget_static_2.setObjectName("matplotlibwidget_static_2")
        self.layoutWidget = QtWidgets.QWidget(self.matplotlibwidget_static_2)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 540, 761, 25))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.horizontalSliderSS = QtWidgets.QSlider(self.layoutWidget)
        self.horizontalSliderSS.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSliderSS.setObjectName("horizontalSliderSS")
        self.horizontalLayout_4.addWidget(self.horizontalSliderSS)
        self.lcdNumberSS = QtWidgets.QLCDNumber(self.layoutWidget)
        self.lcdNumberSS.setObjectName("lcdNumberSS")
        self.horizontalLayout_4.addWidget(self.lcdNumberSS)
        self.wyChooseFile = QtWidgets.QPushButton(self.centralwidget)
        self.wyChooseFile.setGeometry(QtCore.QRect(40, 10, 40, 40))
        self.wyChooseFile.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/pic/img/folder.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.wyChooseFile.setIcon(icon)
        self.wyChooseFile.setIconSize(QtCore.QSize(30, 30))
        self.wyChooseFile.setAutoDefault(False)
        self.wyChooseFile.setObjectName("wyChooseFile")
        self.wyShowArchitecture = QtWidgets.QPushButton(self.centralwidget)
        self.wyShowArchitecture.setGeometry(QtCore.QRect(100, 10, 40, 40))
        self.wyShowArchitecture.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/pic/img/biology.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.wyShowArchitecture.setIcon(icon1)
        self.wyShowArchitecture.setIconSize(QtCore.QSize(30, 30))
        self.wyShowArchitecture.setObjectName("wyShowArchitecture")
        self.wySubsetSelection = QtWidgets.QPushButton(self.centralwidget)
        self.wySubsetSelection.setGeometry(QtCore.QRect(70, 320, 40, 40))
        self.wySubsetSelection.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/pic/img/microscope.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.wySubsetSelection.setIcon(icon2)
        self.wySubsetSelection.setIconSize(QtCore.QSize(30, 30))
        self.wySubsetSelection.setObjectName("wySubsetSelection")
        self.wyPlot = QtWidgets.QPushButton(self.centralwidget)
        self.wyPlot.setGeometry(QtCore.QRect(70, 280, 40, 40))
        self.wyPlot.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/pic/img/brush.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.wyPlot.setIcon(icon3)
        self.wyPlot.setIconSize(QtCore.QSize(30, 30))
        self.wyPlot.setObjectName("wyPlot")
        self.listView = QtWidgets.QListView(self.centralwidget)
        self.listView.setGeometry(QtCore.QRect(30, 100, 121, 171))
        self.listView.setObjectName("listView")
        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(30, 60, 122, 36))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.radioButton = QtWidgets.QRadioButton(self.layoutWidget1)
        self.radioButton.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/pic/img/funnel.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.radioButton.setIcon(icon4)
        self.radioButton.setIconSize(QtCore.QSize(30, 30))
        self.radioButton.setObjectName("radioButton")
        self.horizontalLayout.addWidget(self.radioButton)
        self.radioButton_2 = QtWidgets.QRadioButton(self.layoutWidget1)
        self.radioButton_2.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/pic/img/layers.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.radioButton_2.setIcon(icon5)
        self.radioButton_2.setIconSize(QtCore.QSize(30, 30))
        self.radioButton_2.setObjectName("radioButton_2")
        self.horizontalLayout.addWidget(self.radioButton_2)
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(190, 20, 261, 681))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 259, 679))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.layoutWidget2 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget2.setGeometry(QtCore.QRect(480, 660, 601, 25))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalSliderPatch = QtWidgets.QSlider(self.layoutWidget2)
        self.horizontalSliderPatch.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSliderPatch.setObjectName("horizontalSliderPatch")
        self.horizontalLayout_2.addWidget(self.horizontalSliderPatch)
        self.lcdNumberPatch = QtWidgets.QLCDNumber(self.layoutWidget2)
        self.lcdNumberPatch.setObjectName("lcdNumberPatch")
        self.horizontalLayout_2.addWidget(self.lcdNumberPatch)
        self.layoutWidget3 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget3.setGeometry(QtCore.QRect(480, 690, 601, 25))
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.layoutWidget3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalSliderSlice = QtWidgets.QSlider(self.layoutWidget3)
        self.horizontalSliderSlice.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSliderSlice.setObjectName("horizontalSliderSlice")
        self.horizontalLayout_3.addWidget(self.horizontalSliderSlice)
        self.lcdNumberSlice = QtWidgets.QLCDNumber(self.layoutWidget3)
        self.lcdNumberSlice.setObjectName("lcdNumberSlice")
        self.horizontalLayout_3.addWidget(self.lcdNumberSlice)
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

from test import MatplotlibWidget
import img_rc
