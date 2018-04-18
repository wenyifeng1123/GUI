import theano.tensor as T
import keras.backend as K
from keras.utils.vis_utils import plot_model, model_to_dot
import network_visualization
from network_visualization import *
import theano
import theano.tensor as T
import numpy as np
import matplotlib.pyplot as plt
import h5py
from keras.models import load_model

model = load_model("testout404010_FCN_simple_lr_0.001_bs_64_model.h5")
h=h5py.File("normal404010.h5","r")
X_test=h['X_test'][:]
y_test=h['y_test'][:]
#X_test =np.transpose(np.array(X_test), (1,0,2,3,4))
y_test = np.asarray([y_test[:], np.abs(np.asarray(y_test[:], dtype=np.float32) - 1)]).T
y_test = np.squeeze(y_test, axis=1)
batchSize=5
X_test =np.transpose(np.array(X_test), (1,0,2,3,4))
X_test=X_test[:10] #(1,1632,40,40,10)
y_test=y_test[:10]


score_test, acc_test = model.evaluate(X_test, y_test, batch_size=batchSize, verbose=1)
prob_pre = model.predict(X_test, batch_size=batchSize, verbose=1)

dot = model_to_dot(model, show_shapes=False, show_layer_names=True, rankdir='TB')
layers_by_depth = model.layers_by_depth
maxCol = 0
maxRow = len(layers_by_depth)

for i in range(len(layers_by_depth)):
    for ind,layer in enumerate(layers_by_depth[i]): # the layers in No i layer in the model
        if maxCol < ind:
            maxCow = ind

