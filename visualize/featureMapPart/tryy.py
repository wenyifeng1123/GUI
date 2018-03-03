# -*- coding: utf-8 -*-
import os
import numpy as np
import keras.backend as K
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Activation
from keras.optimizers import SGD, Adam, RMSprop
from keras.utils import np_utils
from keras.layers import Dense, Dropout, Activation, Flatten
from keras.layers import Convolution2D, MaxPooling2D
from network_visualization import on_click,plot_mosaic,get_weights_mosaic,plot_weights,plot_all_weights,plot_feature_map,plot_all_feature_maps
import matplotlib.pyplot as plt

import sys
import random
import matplotlib

matplotlib.use("Qt4Agg")
from PyQt4 import QtCore
from PyQt4.QtCore import pyqtSlot
from PyQt4.QtGui import QApplication, QMainWindow, QVBoxLayout, QSizePolicy, QWidget
from numpy import arange, sin, pi
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
import matplotlib.transforms as mtransforms
import matplotlib.patches as mpatch
from matplotlib.patches import FancyBboxPatch
from Ui_matplotlib_pyqt4 import Ui_MainWindow
import h5py
from keras.models import Sequential, load_model
from keras.utils.vis_utils import plot_model, model_to_dot


def on_click_axes(event):
    """Enlarge or restore the selected axis."""
    model=load_model('m.h5')
    ax = event.inaxes
    if ax is None:
        # Occurs when a region not in an axis is clicked...
        return
    if event.button is 1:

        f = plt.figure()
        if ax.name == 'arrow':
            return

        for l in model.layers:
            if l.name == ax.name:
                w = l.weights

        if len(w) != 0:
            if w[0].ndim == 4:
                w = w[0].container.data
                w = np.transpose(w, (3, 2, 0, 1))
                mosaic_number = w.shape[0]
                nrows = int(np.round(np.sqrt(mosaic_number)))
                ncols = int(nrows)

                if nrows ** 2 < mosaic_number:
                    ncols += 1

                f = plot_mosaic(w[:mosaic_number, 0], nrows, ncols, f)
                plt.suptitle("Weights of Layer '{}'".format(ax.name))
                f.show()
            else:
                pass

        else:
            return

    else:
        # No need to re-draw the canvas if it's not a left or right click
        return
    event.canvas.draw()

class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):

        super(MainWindow, self).__init__(parent)
        self.setupUi(self)

        self.matplotlibwidget_static.setVisible(False)
        self.matplotlibwidget_static_2.setVisible(False)
        self.pushButton_3.hide()
        self.horizontalSlider.hide()

        #self.connect(pushButton, QtCore.SIGNAL('clicked()'), self, QtCore.SLOT('close()'))

        #def on_pushButton_clicked(self):
            #self.matplotlibwidget_static.mpl.start_static_plot()
        self.pushButton.clicked.connect(self.matplotlibwidget_static.mpl.start_static_plot)

    def coco(self):
        self.matplotlibwidget_static.mpl.start_static_plot()



class MyMplCanvas(FigureCanvas):
    """FigureCanvas的最终的父类其实是QWidget。"""

    def __init__(self, parent=None, width=15, height=15):
        # 配置中文显示
        plt.rcParams['font.family'] = ['SimHei']  # 用来正常显示中文标签
        plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

        self.fig = Figure(figsize=(width, height))  # 新建一个figure

        FigureCanvas.__init__(self, self.fig)
        self.setParent(parent)

        '''定义FigureCanvas的尺寸策略，这部分的意思是设置FigureCanvas，使之尽可能的向外填充空间。'''
        FigureCanvas.setSizePolicy(self,
                                   QSizePolicy.Expanding,
                                   QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)

    '''绘制静态图，可以在这里定义自己的绘图逻辑'''

    def start_static_plot(self):
        model=load_model('m.h5')
        layerLength = len(model.layers)
        #fig1 = plt.figure()
        #fig1.show()
        axNumber = layerLength * 2 - 1

        for i in range(axNumber):
            self.axes = self.fig.add_subplot(axNumber, 1, i + 1)  # 建立一个子图，如果要建立复合图，可以在这里修改

            if i % 2 == 0:
                bbox_props = dict(boxstyle="round", fc="w", ec="0.5", alpha=0.9)
                self.axes.text(0.5, 0.5, model.layers[int(i / 2)].name, ha="center", va="center", size=20,
                               bbox=bbox_props)
                self.axes.name = model.layers[int(i / 2)].name
            elif i != axNumber - 1:
                self.axes.annotate('', xy=(0.5, 0), xytext=(0.5, 1),
                                   arrowprops=dict(facecolor='black', shrink=0.05))
                self.axes.name = 'arrow'
            else:
                pass

            self.axes.set_axis_off()

        self.fig.canvas.mpl_connect('button_press_event', on_click_axes)


class MatplotlibWidget(QWidget):
    def __init__(self, parent=None):
        super(MatplotlibWidget, self).__init__(parent)
        self.initUi()

    def initUi(self):
        self.layout = QVBoxLayout(self)
        self.mpl = MyMplCanvas(self, width=15, height=15)
        self.layout.addWidget(self.mpl)






if __name__ == '__main__':
    import sys
    (X_train, y_train), (X_test, y_test) = mnist.load_data()
    # Only take a small part of the data to reduce computation time
    X_train = X_train[:20]
    y_train = y_train[:20]
    X_test = X_test[:20]
    y_test = y_test[:20]

    # Define some variables from the dataset
    nb_classes = np.unique(y_train).shape[0]
    img_rows, img_cols = X_train.shape[-2:]

    X_train = X_train.reshape(X_train.shape[0], 1, img_rows, img_cols).astype('float32')
    X_test = X_test.reshape(X_test.shape[0], 1, img_rows, img_cols).astype('float32')

    X_train /= 255
    X_test /= 255

    print('X_train shape:', X_train.shape)
    print('y_train shape:', y_train.shape)

    # Convert class vectors to binary class matrices
    Y_train = np_utils.to_categorical(y_train, nb_classes)
    Y_test = np_utils.to_categorical(y_test, nb_classes)

    # Model parameters
    nb_filters = 32
    nb_pool = 2
    kernel_size = (3, 3)

    # Create the model
    model = Sequential()
    model.add(Convolution2D(nb_filters, (kernel_size[0], kernel_size[1]),
                            border_mode='valid', activation="relu",
                            input_shape=(1, img_rows, img_cols)))

    model.add(Convolution2D(nb_filters, kernel_size[0], kernel_size[1],
                            border_mode='valid', activation="relu"))

    model.add(MaxPooling2D(pool_size=(nb_pool, nb_pool)))
    model.add(Dropout(0.25))

    model.add(Flatten())

    model.add(Dense(nb_classes))
    model.add(Activation('softmax'))

    model.summary()

    model.compile(loss='categorical_crossentropy',
                  optimizer=RMSprop(),
                  metrics=['accuracy'])

    batch_size = 128
    nb_epoch = 5

    history = model.fit(X_train, Y_train,
                        batch_size=batch_size, nb_epoch=nb_epoch,
                        verbose=1, validation_data=(X_test, Y_test))
    model.save('m.h5')
    ### GUI###
    app = QApplication(sys.argv)
    ui = MainWindow()
    ui.show()
    sys.exit(app.exec_())