# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_matplotlib_pyqt_ListButton.ui'
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
        self.matplotlibwidget_static_2 = MatplotlibWidget(self.centralwidget)
        self.matplotlibwidget_static_2.setGeometry(QtCore.QRect(320, 30, 731, 491))
        self.matplotlibwidget_static_2.setObjectName("matplotlibwidget_static_2")
        self.listView = QtWidgets.QListView(self.centralwidget)
        self.listView.setGeometry(QtCore.QRect(130, 180, 161, 161))
        self.listView.setObjectName("listView")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(170, 360, 75, 23))
        self.pushButton_3.setObjectName("pushButton_3")
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
        self.pushButton_2.clicked.connect(self.matplotlibwidget_static.hide)
        self.pushButton_2.clicked.connect(self.matplotlibwidget_static_2.show)
        self.pushButton.clicked.connect(self.matplotlibwidget_static_2.hide)
        self.pushButton.clicked.connect(self.listView.hide)
        self.pushButton_2.clicked.connect(self.listView.show)
        self.pushButton.clicked.connect(self.pushButton_3.hide)
        self.pushButton_2.clicked.connect(self.pushButton_3.show)
        self.listView.clicked['QModelIndex'].connect(self.matplotlibwidget_static_2.show)
        self.pushButton_3.clicked.connect(self.matplotlibwidget_static_2.show)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "weights"))
        self.pushButton_2.setText(_translate("MainWindow", "archietecture"))
        self.pushButton_3.setText(_translate("MainWindow", "PushButton"))

from matplotlibwidget import MatplotlibWidget
