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

modelDimension =[]
model = load_model("testout404010_FCN_simple_lr_0.001_bs_64_model.h5")
h=h5py.File("normal404010.h5","r")
X_test=h['X_test'][:]
y_test=h['y_test'][:]
#X_test =np.transpose(np.array(X_test), (1,0,2,3,4))
y_test = np.asarray([y_test[:], np.abs(np.asarray(y_test[:], dtype=np.float32) - 1)]).T
y_test = np.squeeze(y_test, axis=1)
batchSize=5
X_test =np.transpose(np.array(X_test), (1,0,2,3,4))
X_test=X_test[:5] #(5,1,40,40,10)
y_test=y_test[:5]

score_test, acc_test = model.evaluate(X_test, y_test, batch_size=batchSize, verbose=1)
prob_pre = model.predict(X_test, batch_size=batchSize, verbose=1)

h3=h5py.File('test3D.h5','w')
if len(X_test)==4:
    modelDimension.append('2D')
    modelDimension=h3.create_dataset('modelDimension',data=modelDimension)
elif len(X_test)==5:
    modelDimension.append('3D')
    modelDimension=h3.create_dataset('modelDimension', data=modelDimension)
else:
    print("the dimesnion should be 2D or 3D")
#save the features
activation={}
act=h3.create_group('activations')
for i,layer in enumerate(model.layers):
    get_activations = K.function([model.input, K.learning_phase()], [layer.output, ])
    activation[layer.name]=get_activations([X_test, 0])[0]
    a = act.create_dataset(layer.name, data=activation[layer.name])


dot = model_to_dot(model, show_shapes=False, show_layer_names=True, rankdir='TB')
layers_by_depth = model.layers_by_depth


layer_by_depth=h3.create_group('layer_by_depth')
weights=h3.create_group('weights')

maxCol = 0
maxRow = len(layers_by_depth)
## Save the structure,weights the layers' names in .h5 file
for i in range(len(layers_by_depth)):
    i_layer = layer_by_depth.create_group(str(i)) #the No i layer  in the model
    for ind,layer in enumerate(layers_by_depth[i]): # the layers in No i layer in the model
        if maxCol < ind:
            maxCow = ind
        i_ind=i_layer.create_group(str(ind))
        layer_name=i_ind.create_dataset('layer_name', data=layer.name)
        if len(layer.weights)==0:
            w=0
        else:
            w=layer.weights[0].container.data
        weights.create_dataset(layer.name,data=w) # save the weights
        #allLayerNames.append(layer.name)


class_idx = 0
reg_param = 1 / (2e-4)
output =T.dmatrix('output')
output=model.output
input = model.input
cost  = -T.sum(T.log(input[:,class_idx]+1e-8))
gradient = theano.tensor.grad(cost, input)
calcCost = theano.function([input], cost)
calcGrad = theano.function([input], gradient)

#2. Use subset selection:

step_size = 0.019
reg_param = 1/(2e-4)
test=X_test[:]

data_c = test
oss_v = network_visualization.SubsetSelection(calcGrad, calcCost, data_c, alpha=reg_param, gamma=step_size)
result = oss_v.optimize(np.random.uniform(0, 1.0, size=data_c.shape))
h3.create_dataset('subset_selection', data=result)
h3.close()

