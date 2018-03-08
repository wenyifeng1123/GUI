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

matplotlib.use("Qt5Agg")
from PyQt5 import QtCore
from PyQt5.QtCore import pyqtSlot,QStringListModel
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QSizePolicy, QWidget, QListView
from numpy import arange, sin, pi
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
#from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbarfrom matplotlib.figure import Figure
import matplotlib.transforms as mtransforms
import matplotlib.patches as mpatch
from matplotlib.patches import FancyBboxPatch
from Ui_matplotlib_pyqt_List import Ui_MainWindow
import h5py
from keras.models import Sequential, load_model
from keras.utils.vis_utils import plot_model, model_to_dot
from network_visualization import plot_mosaic


def getLayersWeights():
    model = h5py.File('layer2ge.h5', 'r')
    layersName = []
    layersWeights = {}

    for i in model['layers']:
        layerIndex = 'layers' + '/' + i

        for n in model[layerIndex]:
            layerName = layerIndex + '/' + n
            layersName.append(n)

            weightsPath = layerName + '/' + 'weights'
            layersWeights[n] = model[weightsPath]
    #model.close()
    return layersName,layersWeights

def on_click_axes(event):
    """Enlarge or restore the selected axis."""

    ax = event.inaxes
    layersName, layersWeights = getLayersWeights()
    if ax is None:
        # Occurs when a region not in an axis is clicked...
        return
    if event.button is 1:
        #event.canvas.matplotlibwidget_static_2.setVisible(True)
        f = plt.figure()
        if ax.name=='arrow':
            return

        w = layersWeights[ax.name].value
        if w.ndim == 4:
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
        # No need to re-draw the canvas if it's not a left or right click
        return
    event.canvas.draw()

class MainWindow(QMainWindow, Ui_MainWindow):
    """
    Class documentation goes here.
    """

    def __init__(self, parent=None):
        """
        Constructor
        @param parent reference to the parent widget
        @type QWidget
        """
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)

        self.matplotlibwidget_static.hide()
        self.matplotlibwidget_static_2.hide()
        self.listView.hide()


        #self.horizontalSlider.hide()
    @pyqtSlot()
    def on_pushButton_clicked(self):
        self.matplotlibwidget_static_2.hide()
        self.listView.hide()
        self.matplotlibwidget_static.mpl.weights_plot()

    @pyqtSlot()
    def on_pushButton_2_clicked(self):
        self.matplotlibwidget_static_2.setVisible(True)
        self.matplotlibwidget_static.hide()

        self.matplotlibwidget_static_2.mpl.feature_plot()

        self.listView.show()
        slm = QStringListModel();
        self.qList =self.show_activation_names()
        slm.setStringList(self.qList)
        self.listView.setModel(slm)

    def show_activation_names(self):
        qList=[]
        model = h5py.File('layer2ge.h5', 'r')

        for i in model['layers']:
            layerIndex = 'layers' + '/' + i

            for n in model[layerIndex]:
                qList.append(n)

        return qList


class MyMplCanvas(FigureCanvas):
    """FigureCanvas的最终的父类其实是QWidget。"""

    def __init__(self, parent=None, width=15, height=15):
        # 配置中文显示
        plt.rcParams['font.family'] = ['SimHei']  # 用来正常显示中文标签
        plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

        self.fig = plt.figure(figsize=(width, height))  # 新建一个figure

        FigureCanvas.__init__(self, self.fig)
        self.setParent(parent)

        '''定义FigureCanvas的尺寸策略，这部分的意思是设置FigureCanvas，使之尽可能的向外填充空间。'''
        FigureCanvas.setSizePolicy(self,
                                   QSizePolicy.Expanding,
                                   QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)

    '''绘制静态图，可以在这里定义自己的绘图逻辑'''

    def weights_plot(self):

        layersName, layersWeights = getLayersWeights()
        layerLength = len(layersName)
        spacing = 1.2
        axNumber = layerLength * 2 - 1

        for i in range(axNumber):

            self.axes = self.fig.add_subplot(axNumber, 1, i + 1)  # 建立一个子图，如果要建立复合图，可以在这里修改

            if i % 2 == 0:
                bbox_props = dict(boxstyle="round", fc="w", ec="0.5", alpha=0.9)
                self.axes.text(0.5, 0.5, layersName[int(i / 2)], ha="center", va="center", size=20,
                               bbox=bbox_props)
                self.axes.name = layersName[int(i / 2)]
            elif i != axNumber - 1:
                self.axes.annotate('', xy=(0.5, 0), xytext=(0.5, 1),
                                   arrowprops=dict(facecolor='black', shrink=0.05))
                self.axes.name = 'arrow'
            else:
                pass

            self.axes.set_axis_off()

        self.fig.canvas.mpl_connect('button_press_event', on_click_axes)

    def feature_plot(self):
        layersName, activations = self.getLayersFeatures()
        for feature_map in layersName:
            if activations[feature_map].ndim == 4:

                for ind,featMap in enumerate(activations[feature_map]):

                    # Compute nrows and ncols for images
                    n_mosaic = len(featMap)
                    nrows = int(np.round(np.sqrt(n_mosaic)))
                    ncols = int(nrows)
                    if (nrows ** 2) < n_mosaic:
                        ncols += 1

                    plot_mosaic(featMap, nrows, ncols, self.fig)

            else:
                pass




    def getLayersFeatures(self):
        model = h5py.File('layer2ge.h5', 'r')
        layersName = []
        layersFeatures = {}

        for i in model['layers']:
            layerIndex = 'layers' + '/' + i

            for n in model[layerIndex]:
                layerName = layerIndex + '/' + n
                layersName.append(n)

                featurePath = layerName + '/' + 'activation'
                layersFeatures[n] = model[featurePath]
        # model.close()
        return layersName, layersFeatures


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
    app = QApplication(sys.argv)
    ui = MainWindow()
    ui.show()
    sys.exit(app.exec_())
