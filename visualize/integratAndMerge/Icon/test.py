# -*- coding: utf-8 -*-
import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use("Qt5Agg")
from PyQt5 import QtCore
from PyQt5.QtCore import pyqtSlot,QStringListModel,pyqtSignal
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QSizePolicy, QWidget, QListView,QMessageBox,QFileDialog,QDialog,QPushButton
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from Ui_2 import Ui_MainWindow
import h5py
from keras.utils.vis_utils import plot_model, model_to_dot
from keras.models import load_model

#from network_visualization import plot_mosaic,on_click


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
        self.scrollArea.hide()
        self.horizontalSlider.hide()
        self.lcdNumber.hide()

        self.chosenLayerName = []
        # the slider's value is the chosen patch's number
        self.chosenPatchNumber = 1
        self.openfile_name=''

        self.model={}
        self.qList=[]
        self.totalPatches=0
        self.activations = {}
        self.radioButtonValue=[]
        self.listView.clicked.connect(self.clickList)

        # from the .h5 file extract the name of each layer and the total number of patches
        #self.wy1.clicked.connect(self.openfile)

        #self.horizontalSlider.valueChanged.connect(self.sliderValue)
        self.horizontalSlider.sliderReleased.connect(self.sliderValue)
        self.horizontalSlider.valueChanged.connect(self.lcdNumber.display)



    def clickList(self,qModelIndex):

        self.chosenLayerName = self.qList[qModelIndex.row()]


    def show_layer_names(self):
        qList = []
        totalPatches = 0
        activations = self.model['activations']

        for i in activations:
            qList.append(i)
            layerPath = 'activations' + '/' + i
            self.activations[i] = self.model[layerPath]
            if totalPatches < len(self.activations[i]):
                totalPatches = len(self.activations[i])

        self.qList = qList
        self.totalPatches = totalPatches

    def sliderValue(self):
        self.chosenPatchNumber=self.horizontalSlider.value()
        self.matplotlibwidget_static.mpl.features_plot(self.activations, self.chosenLayerName, self.chosenPatchNumber)


    @pyqtSlot()
    def on_wyChooseFile_clicked(self):
        self.openfile_name = QFileDialog.getOpenFileName(self,'Choose the file','.','H5 files(*.h5)')[0]
        if len(self.openfile_name)==0:
            pass
        else:
            self.model=h5py.File(self.openfile_name,'r')
            self.qList, self.totalPatches = self.show_layer_names()
            self.horizontalSlider.setMinimum(1)
            self.horizontalSlider.setMaximum(self.totalPatches)
            # show the activations' name in the List
            slm = QStringListModel();
            slm.setStringList(self.qList)
            self.listView.setModel(slm)

            self.horizontalSlider.setMinimum(1)
            self.horizontalSlider.setMaximum(self.totalPatches)

    @pyqtSlot()
    def on_wyShowArchitecture_clicked(self):
        # Show the structure of the model and plot the weights
        if len(self.openfile_name) != 0:
            # show the weights
            self.matplotlibwidget_static_2.hide()
            self.matplotlibwidget_static.hide()
            self.scrollArea.show()

        else:
            self.showChooseFileDialog()

    @pyqtSlot()
    def on_wyPlot_clicked(self):
        self.matplotlibwidget_static_2.hide()
        self.scrollArea.show()

        # Show the structure of the model and plot the weights
        if len(self.openfile_name) != 0:
            if self.radioButton.isChecked()== True :
                if len(self.chosenLayerName) != 0:

                    # show the weights
                    self.lcdNumber.hide()
                    self.horizontalSlider.hide()
                    self.matplotlibwidget_static.show()
                    self.matplotlibwidget_static.mpl.weights_plot(self.model,self.chosenLayerName)

                else:
                    self.showChooseLayerDialog()

            elif self.radioButton_2.isChecked()== True :
                if len(self.chosenLayerName) != 0:

                    self.horizontalSlider.show()
                    self.lcdNumber.show()
                    # show the features
                    self.matplotlibwidget_static.show()
                    self.matplotlibwidget_static.mpl.features_plot(self.activations, self.chosenLayerName, self.chosenPatchNumber)

                else:
                    self.showChooseLayerDialog()

            else:
                self.showChooseButtonDialog()

        else:
            self.showChooseFileDialog()

    @pyqtSlot()
    def on_wySubsetSelection_clicked(self):
        # Show the Subset Selection
        if len(self.openfile_name) != 0:
            # show the weights
            self.scrollArea.hide()
            self.lcdNumber.hide()
            self.horizontalSlider.hide()
            self.matplotlibwidget_static.hide()
            self.matplotlibwidget_static_2.show()
            self.matplotlibwidget_static_2.mpl.subset_selection_plot(self.model)
        else:
            self.showChooseFileDialog()

    def clickList_1(self, qModelIndex):
        self.chosenActivationName = self.qList[qModelIndex.row()]

    def show_layer_names(self):
        qList = []
        totalPatches = 0
        activations = self.model['activations']

        for i in activations:
            qList.append(i)
            layerPath = 'activations' + '/' + i
            self.activations[i] = self.model[layerPath]
            if totalPatches < len(self.activations[i]):
                totalPatches =len(self.activations[i])

        return qList, totalPatches

    def showChooseFileDialog(self):
        reply = QMessageBox.information(self,
                                        "Warning",
                                        "Please select one H5 File at first",
                                        QMessageBox.Ok )

    def showChooseLayerDialog(self):
        reply = QMessageBox.information(self,
                                        "Warning",
                                        "Please select one Layer at first",
                                        QMessageBox.Ok)

    def showChooseButtonDialog(self):
        reply = QMessageBox.information(self,
                                        "Warning",
                                        "Please select to plot the weights or the features",
                                        QMessageBox.Ok)

class MyMplCanvas(FigureCanvas):

    def __init__(self, parent=None, width=15, height=15):

        plt.rcParams['font.family'] = ['SimHei']
        plt.rcParams['axes.unicode_minus'] = False

        self.fig = plt.figure(figsize=(width, height))
        #self.openfile_name=''
        self.model = {}
        self.layerWeights = {}  # {layer name: weights value}
        self.edgesInLayerName = [] #(input layer name, output layer name)
        self.allLayerNames = []
        self.axesDict = {}
        self.activations = {}
        self.matplotlibwidget_static_2={}
        self.mainSelf={}
        self.chosenLayerName=[]

        FigureCanvas.__init__(self, self.fig)
        self.setParent(parent)

        FigureCanvas.setSizePolicy(self,QSizePolicy.Expanding,QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)



    def weights_plot(self,model,chosenLayerName):
        self.fig.clf()
        self.model = model
        self.chosenLayerName=chosenLayerName
        self.getLayersWeights()
        self.fig.suptitle("Weights of Layer '{}'".format(self.chosenLayerName))
        w = self.layerWeights[self.chosenLayerName]
        if w.ndim == 4:

            w = np.transpose(w, (3, 2, 0, 1))
            mosaic_number = w.shape[0]
            nrows = int(np.round(np.sqrt(mosaic_number)))
            ncols = int(nrows)

            if nrows ** 2 < mosaic_number:
                ncols += 1

            self.fig = self.plot_weight_mosaic(w[:mosaic_number, 0], nrows, ncols, self.fig)
            self.draw()

        else:
            pass

    def features_plot(self,activations, chosenLayerName, chosenPatchNumber):

        self.activations=activations
        ind = chosenPatchNumber-1

        if activations[chosenLayerName].ndim == 4:
            featMap=activations[chosenLayerName][ind]

            # Compute nrows and ncols for images
            n_mosaic = len(featMap)
            nrows = int(np.round(np.sqrt(n_mosaic)))
            ncols = int(nrows)
            if (nrows ** 2) < n_mosaic:
                ncols += 1

            self.fig.clear()
            # self.draw()
            # self.show()
            self.plot_feature_mosaic(featMap, nrows, ncols)
            self.fig.suptitle("Feature Maps of Patch #{} in Layer '{}'".format(ind+1, chosenLayerName))
            self.draw()
        else:
            pass

    def subset_selection_plot(self,model):
        self.model=model
        subset_selection=self.getSubsetSelections()
        nimgs = len(subset_selection)
        nrows = int(np.round(np.sqrt(nimgs)))
        ncols = int(nrows)
        if (nrows ** 2) < nimgs:
            ncols += 1

        self.fig=self.plot_subset_mosaic(subset_selection, nrows, ncols, self.fig)

    def getLayersWeights(self):
        weights = self.model['weights']
        for i in weights:
            p = 'weights' + '/' + i
            self.layerWeights[i] = self.model[p]

    def getLayersFeatures(self):
        model = h5py.File(self.openfile_name, 'r')
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

    def getSubsetSelections(self):

        subset_selection=self.model['subset_selection']
        return subset_selection

    def plot_weight_mosaic(self,im, nrows, ncols, fig,**kwargs):

        # Set default matplotlib parameters
        if not 'interpolation' in kwargs.keys():
            kwargs['interpolation'] = "none"

        if not 'cmap' in kwargs.keys():
            kwargs['cmap'] = "gray"

        nimgs = len(im)
        imshape = im[0].shape

        mosaic = np.zeros(imshape)

        for i in range(nimgs):
            row = int(np.floor(i / ncols))
            col = i % ncols

            ax = fig.add_subplot(nrows, ncols,i+1)
            ax.set_xlim(0,imshape[0]-1)
            ax.set_ylim(0,imshape[1]-1)

            mosaic = im[i]

            ax.imshow(mosaic, **kwargs)
            ax.set_axis_off()

        fig.canvas.mpl_connect('button_press_event', self.on_click)
        return fig

    def plot_feature_mosaic(self,im, nrows, ncols, **kwargs):

        # Set default matplotlib parameters
        if not 'interpolation' in kwargs.keys():
            kwargs['interpolation'] = "none"

        if not 'cmap' in kwargs.keys():
            kwargs['cmap'] = "gray"

        nimgs = len(im)
        imshape = im[0].shape

        mosaic = np.zeros(imshape)
        #fig.clear()

        for i in range(nimgs):
            row = int(np.floor(i / ncols))
            col = i % ncols

            ax = self.fig.add_subplot(nrows, ncols,i+1)
            ax.set_xlim(0,imshape[0]-1)
            ax.set_ylim(0,imshape[1]-1)

            mosaic = im[i]

            ax.imshow(mosaic, **kwargs)
            ax.set_axis_off()
        self.draw()
        self.fig.canvas.mpl_connect('button_press_event', self.on_click)

    def plot_subset_mosaic(self,im,nrows, ncols, fig,**kwargs):
        if not 'interpolation' in kwargs.keys():
            kwargs['interpolation'] = "none"

        if not 'cmap' in kwargs.keys():
            kwargs['cmap'] = "gray"
        im = np.squeeze(im, axis=1)
        nimgs = len(im)
        imshape = im[0].shape

        mosaic = np.zeros(imshape)

        for i in range(nimgs):
            row = int(np.floor(i / ncols))
            col = i % ncols

            ax = fig.add_subplot(nrows, ncols, i + 1)
            ax.set_xlim(0, imshape[0] - 1)
            ax.set_ylim(0, imshape[1] - 1)

            mosaic = im[i]

            ax.imshow(mosaic, **kwargs)
            ax.set_axis_off()
        # fig.suptitle("Subset Selection of Patch #{} in Layer '{}'".format(ind, feature_map))
        fig.canvas.mpl_connect('button_press_event', self.on_click)
        return fig

    def on_click(self,event):
        """Enlarge or restore the selected axis."""
        ax = event.inaxes
        if ax is None:
            # Occurs when a region not in an axis is clicked...
            return
        if event.button is 1:
            # On left click, zoom the selected axes
            ax._orig_position = ax.get_position()
            ax.set_position([0.1, 0.1, 0.85, 0.85])
            for axis in event.canvas.figure.axes:
                # Hide all the other axes...
                if axis is not ax:
                    axis.set_visible(False)
        elif event.button is 3:
            # On right click, restore the axes
            try:
                ax.set_position(ax._orig_position)
                for axis in event.canvas.figure.axes:
                    axis.set_visible(True)
            except AttributeError:
                # If we haven't zoomed, ignore...
                pass
        else:
            # No need to re-draw the canvas if it's not a left or right click
            return
        event.canvas.draw()



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
