# -*- coding: utf-8 -*-
import os
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
matplotlib.use("Qt5Agg")
from PyQt5 import QtCore,QtWidgets
from PyQt5.QtCore import pyqtSlot,QStringListModel,pyqtSignal
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QSizePolicy, QWidget, QListView,QMessageBox,QFileDialog,QDialog,QPushButton
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from Ui_3 import Ui_MainWindow
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
        #self.scrollArea.hide()
        self.horizontalSliderPatch.hide()
        self.horizontalSliderSlice.hide()
        self.horizontalSliderSS.hide()

        self.lcdNumberPatch.hide()
        self.lcdNumberSlice.hide()
        self.lcdNumberSS.hide()

        self.resetW=False
        self.resetF = False
        self.resetS = False

        self.chosenLayerName = []
        # the slider's value is the chosen patch's number
        self.chosenPatchNumber = 1
        self.chosenSSNumber = 1
        self.openfile_name=''

        self.model={}
        self.qList=[]
        self.totalPatches=0
        self.totalSS=0

        self.modelDimension= ''
        self.activations = {}
        self.weights ={}
        self.subset_selection = {}
        self.radioButtonValue=[]
        self.listView.clicked.connect(self.clickList)



        # slider of the feature
        self.horizontalSliderPatch.sliderReleased.connect(self.sliderValue)
        self.horizontalSliderPatch.valueChanged.connect(self.lcdNumberPatch.display)
        self.matplotlibwidget_static.mpl.wheel_scroll_signal.connect(self.wheelScroll)

        # slider of the Subset Selection
        self.horizontalSliderSS.sliderReleased.connect(self.sliderValueSS)
        self.horizontalSliderSS.valueChanged.connect(self.lcdNumberSS.display)
        self.matplotlibwidget_static_2.mpl.wheel_scroll_SS_signal.connect(self.wheelScrollSS)


        #self.lab=QLabel()
        #self.lab.setPixmap(QPixmap("4040.png"))
        '''
        self.vbox=QVBoxLayout()
        self.vbox.addWidget(self.lab)
        self.widget.setLayout(self.vbox)
        self.widget.show()'''

        self.canvasStructure=MyMplCanvas()
        self.canvasStructure.loadImage()
        self.graphicscene = QtWidgets.QGraphicsScene()
        self.graphicscene.addWidget(self.canvasStructure)
        self.graphicsView.setScene(self.graphicscene)


    def wheelScroll(self,ind):
        self.horizontalSliderPatch.setValue(ind)
        self.horizontalSliderPatch.valueChanged.connect(self.lcdNumberPatch.display)

    def wheelScrollSS(self,indSS):
        self.horizontalSliderSS.setValue(indSS)
        self.horizontalSliderSS.valueChanged.connect(self.lcdNumberSS.display)

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
        self.chosenPatchNumber=self.horizontalSliderPatch.value()
        self.matplotlibwidget_static.mpl.features_plot(self.activations, self.chosenLayerName, self.chosenPatchNumber,self.totalPatches)

    def sliderValueSS(self):
        self.chosenSSNumber=self.horizontalSliderSS.value()
        self.matplotlibwidget_static_2.mpl.subset_selection_plot(self.chosenSSNumber,self.totalSS)

    @pyqtSlot()
    def on_wyChooseFile_clicked(self):
        self.openfile_name = QFileDialog.getOpenFileName(self,'Choose the file','.','H5 files(*.h5)')[0]
        if len(self.openfile_name)==0:
            pass
        else:
            self.resetW = True
            self.resetF = True
            self.resetS = True

            self.model=h5py.File(self.openfile_name,'r')
            # self.model['modelDimension'] = str(self.model['modelDimension'].value)[3:5]
            a=self.model['modelDimension'].value
            self.modelDimension=str(a)[3:5]
            self.weights =self.model['weights']

            self.qList, self.totalPatches = self.show_layer_names()
            self.subset_selection =self.model['subset_selection']
            self.subset_selection = np.squeeze(self.subset_selection, axis=1)
            self.totalSS = len(self.subset_selection)

            # set the patch value of the feature map
            self.horizontalSliderPatch.setMinimum(1)
            self.horizontalSliderPatch.setMaximum(self.totalPatches)

            # set the patch value of the Subset Selection
            self.horizontalSliderSS.setMinimum(1)
            self.horizontalSliderSS.setMaximum(self.totalSS)
            # show the activations' name in the List
            slm = QStringListModel();
            slm.setStringList(self.qList)
            self.listView.setModel(slm)

    @pyqtSlot()
    def on_wyShowArchitecture_clicked(self):
        # Show the structure of the model and plot the weights
        if len(self.openfile_name) != 0:
            # show the weights
            self.matplotlibwidget_static_2.hide()
            self.matplotlibwidget_static.hide()
            self.matplotlibwidget_static_3.show()
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
                    self.lcdNumberPatch.hide()
                    self.horizontalSliderPatch.hide()
                    self.matplotlibwidget_static.show()

                    if self.modelDimension == '2D':
                        self.matplotlibwidget_static.mpl.weights_plot(self.weights,self.chosenLayerName)
                    elif self.modelDimension == '3D':
                        self.horizontalSliderSlice.show()
                        self.lcdNumberSlice.show()
                        self.matplotlibwidget_static.mpl.weights_plot(self.weights, self.chosenLayerName)
                    else:
                        print('the dimesnion should be 2D or 3D')

                else:
                    self.showChooseLayerDialog()

            elif self.radioButton_2.isChecked()== True :
                if len(self.chosenLayerName) != 0:

                    self.horizontalSliderPatch.show()
                    self.lcdNumberPatch.show()
                    # show the features
                    self.matplotlibwidget_static.show()
                    self.matplotlibwidget_static.mpl.features_plot(self.activations, self.chosenLayerName, self.chosenPatchNumber,self.totalPatches)

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
            self.lcdNumberPatch.hide()
            self.lcdNumberSlice.hide()
            self.horizontalSliderPatch.hide()
            self.horizontalSliderSlice.hide()
            self.matplotlibwidget_static.hide()
            self.matplotlibwidget_static_2.show()
            self.horizontalSliderSS.show()
            self.lcdNumberSS.show()
            if self.resetS == True:
                self.matplotlibwidget_static_2.mpl.getSubsetSelections(self.subset_selection)
                self.resetS=False
            self.matplotlibwidget_static_2.mpl.subset_selection_plot(self.chosenSSNumber, self.totalSS)
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
    wheel_scroll_signal = pyqtSignal(int)
    wheel_scroll_SS_signal = pyqtSignal(int)
    def __init__(self, parent=None, width=15, height=15):

        plt.rcParams['font.family'] = ['SimHei']
        plt.rcParams['axes.unicode_minus'] = False

        self.fig = plt.figure(figsize=(width, height))
        #self.openfile_name=''
        self.model = {}

        self.w_count=0
        self.f_count=0
        self.s_count=0
        self.layerWeights = {}  # {layer name: weights value}
        self.edgesInLayerName = [] #(input layer name, output layer name)
        self.allLayerNames = []
        self.axesDict = {}

        self.activations = {}
        self.weights ={}
        self.subset_selection = {}

        self.chosenLayerName=[]

        self.ind =0
        self.nrows = 0
        self.ncols = 0
        self.totalPatches = 0

        # subset selection parameters
        self.totalSS =0
        self.chosenSSNumber =0


        FigureCanvas.__init__(self, self.fig)
        self.setParent(parent)

        FigureCanvas.setSizePolicy(self,QSizePolicy.Expanding,QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)

    def loadImage(self):

        strImg = mpimg.imread('4040.png')
        plt.imshow(strImg)


    def weights_plot(self,weights,chosenLayerName):
        self.fig.clf()
        self.weights = weights
        self.chosenLayerName=chosenLayerName
        if self.w_count == 0:
            self.getLayersWeights()
        self.plot_weight_mosaic()


    def features_plot(self,activations, chosenLayerName, chosenPatchNumber,totalPatches):

        self.activations=activations
        self.ind = chosenPatchNumber-1
        self.chosenLayerName=chosenLayerName
        self.totalPatches = totalPatches

        if activations[chosenLayerName].ndim == 4:
            featMap=activations[chosenLayerName][self.ind]

            # Compute nrows and ncols for images
            n_mosaic = len(featMap)
            self.nrows = int(np.round(np.sqrt(n_mosaic)))
            self.ncols = int(self.nrows)
            if (self.nrows ** 2) < n_mosaic:
                self.ncols += 1

            self.fig.clear()
            self.plot_feature_mosaic(featMap, self.nrows, self.ncols)
            self.fig.suptitle("Feature Maps of Patch #{} in Layer '{}'".format(self.ind+1, self.chosenLayerName))
            self.draw()
        else:
            pass

    def subset_selection_plot(self, chosenSSNumber, totalSS):

        self.chosenSSNumber =chosenSSNumber
        self.totalSS = totalSS
        self.indSS = self.chosenSSNumber - 1
        ss = self.subset_selection[self.indSS]

        self.fig.clear()
        self.plot_subset_mosaic(ss)
        self.draw()

    def plot_weight_mosaic(self,**kwargs):

        # Set default matplotlib parameters
        if not 'interpolation' in kwargs.keys():
            kwargs['interpolation'] = "none"

        if not 'cmap' in kwargs.keys():
            kwargs['cmap'] = "gray"

        #self.fig.suptitle("Weights of Layer '{}'".format(self.chosenLayerName))
        w = self.layerWeights[self.chosenLayerName]
        if w.ndim == 4:

            w = np.transpose(w, (3, 2, 0, 1))
            mosaic_number = w.shape[0]
            w = w[:mosaic_number, 0]
            nrows = int(np.round(np.sqrt(mosaic_number)))
            ncols = int(nrows)

            if nrows ** 2 < mosaic_number:
                ncols += 1

            imshape = w[0].shape

            for i in range(mosaic_number):

                ax = self.fig.add_subplot(nrows, ncols, i + 1)
                ax.set_xlim(0, imshape[0] - 1)
                ax.set_ylim(0, imshape[1] - 1)

                mosaic = w[i]

                ax.imshow(mosaic, **kwargs)
                ax.set_axis_off()

            self.fig.suptitle("Weights of Layer '{}'".format(self.chosenLayerName))
            self.draw()

        else:
            pass

        self.fig.canvas.mpl_connect('button_press_event', self.on_click)

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
        self.fig.canvas.mpl_connect('scroll_event', self.onscroll)

    def plot_subset_mosaic(self,im,**kwargs):
        if not 'interpolation' in kwargs.keys():
            kwargs['interpolation'] = "none"

        if not 'cmap' in kwargs.keys():
            kwargs['cmap'] = "gray"

        if len(im.shape) ==2:
            imshape = im.shape

            ax = self.fig.add_subplot(111)
            ax.set_xlim(0, imshape[0] - 1)
            ax.set_ylim(0, imshape[1] - 1)
            ax.imshow(im, **kwargs)
            ax.set_axis_off()

        elif len(im.shape) ==3:
            im=np.transpose(im,(2,0,1))
            nimgs=im.shape[0]
            imshape = im[0].shape
            nrows = int(np.round(np.sqrt(nimgs)))
            ncols = int(nrows)
            if (nrows ** 2) < nimgs:
                ncols += 1

            for i in range(nimgs):

                ax = self.fig.add_subplot(nrows, ncols, i + 1)
                ax.set_xlim(0, imshape[0] - 1)
                ax.set_ylim(0, imshape[1] - 1)

                mosaic = im[i]

                ax.imshow(mosaic, **kwargs)
                ax.set_axis_off()
        else:
            print('the dimension of the subset selection is not right')

        self.fig.suptitle("Subset Selection of Patch #{}".format(self.indSS+1))
        self.fig.canvas.mpl_connect('button_press_event', self.on_click)
        self.fig.canvas.mpl_connect('scroll_event', self.onscrollSS)

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

    def onscrollSS(self, event):
        if event.button == 'up':
            if self.indSS == (self.totalSS-1):
                pass
            else:
                self.indSS+= 1
            ss = self.subset_selection[self.indSS]
            self.fig.clear()
            self.plot_subset_mosaic(ss)
            self.draw()
            self.wheel_scroll_signal.emit(self.ind+1)
            self.wheel_scroll_SS_signal.emit(self.indSS+1)


        elif event.button == 'down':
            if self.indSS -1<0:
                self.indSS =0
            else:
                self.indSS -= 1
            ss = self.subset_selection[self.indSS]
            self.fig.clear()
            self.plot_subset_mosaic(ss)
            # self.fig.suptitle("Feature Maps of Patch #{} in Layer '{}'".format(self.ind + 1, self.chosenLayerName))
            self.draw()
            self.wheel_scroll_SS_signal.emit(self.indSS+1)
        else:
            pass

    def onscroll(self, event):
        if event.button == 'up':
            if self.ind == (self.totalPatches - 1):
                pass
            else:
                self.ind += 1
            featMap = self.activations[self.chosenLayerName][self.ind]
            self.fig.clear()
            self.plot_feature_mosaic(featMap, self.nrows, self.ncols)
            self.fig.suptitle("Feature Maps of Patch #{} in Layer '{}'".format(self.ind + 1, self.chosenLayerName))
            self.draw()
            self.wheel_scroll_signal.emit(self.ind + 1)


        elif event.button == 'down':
            if self.ind - 1 < 0:
                self.ind = 0
            else:
                self.ind -= 1
            featMap = self.activations[self.chosenLayerName][self.ind]
            self.fig.clear()
            self.plot_feature_mosaic(featMap, self.nrows, self.ncols)
            self.fig.suptitle("Feature Maps of Patch #{} in Layer '{}'".format(self.ind + 1, self.chosenLayerName))
            self.draw()
            self.wheel_scroll_signal.emit(self.ind + 1)
        else:
            pass

    def getLayersWeights(self):
        for i in self.weights:
            self.layerWeights[i] = self.weights[i]

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

    def getSubsetSelections(self,subset_selection):
        self.subset_selection = subset_selection


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
