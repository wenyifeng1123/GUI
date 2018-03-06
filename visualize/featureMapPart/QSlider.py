#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtGui, QtCore


class SliderLabel(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Slider Label')
        self.slider = QtGui.QSlider(QtCore.Qt.Horizontal, self)
        self.slider.setFocusPolicy(QtCore.Qt.NoFocus)
        self.slider.setGeometry(30, 40, 100, 30)
        self.connect(self.slider, QtCore.SIGNAL('valueChanged(int)'),
                     self.changeValue)
        self.label = QtGui.QLabel(self)
        self.label.setPixmap(QtGui.QPixmap('mute.png'))
        self.label.setGeometry(160, 25, 64, 64)

    def changeValue(self):
        pos = self.slider.value()
        if pos == 0:
            self.label.setPixmap(QtGui.QPixmap('mute.png'))
        elif pos <= 30:
            self.label.setPixmap(QtGui.QPixmap('min.png'))
        elif pos < 80:
            self.label.setPixmap(QtGui.QPixmap('med.png'))
        else:
            self.label.setPixmap(QtGui.QPixmap('max.png'))


app = QtGui.QApplication(sys.argv)
sl = SliderLabel()
sl.show()
sys.exit(app.exec_())