import theano.tensor as T
import keras.backend as K
from keras.utils.vis_utils import plot_model, model_to_dot
import network_visualization
from network_visualization import *
import theano
import numpy as np
import matplotlib.pyplot as plt
import h5py
from keras.models import load_model
from keras.utils import plot_model


def plot_subset_mosaic( im, nrows, ncols, fig, **kwargs):
    # Set default matplotlib parameters
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
    #fig.suptitle("Subset Selection of Patch #{} in Layer '{}'".format(ind, feature_map))
    fig.canvas.mpl_connect('button_press_event', on_click)
    return fig

def on_click(event):
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


batchSize=20
model=load_model('testout4040_lr_0.0005_bs_128_model.h5')
# plot_model(model,'M2D.png',show_shapes='true')
#weight_name = '/no_backup/d1240/testout8080/testout8080_lr_0.0001_bs_128_weights.h5'


with h5py.File('crossVal4040.h5','r') as hf:
    # X_test = hf['X_test'][:,2160:2200,:,:]
    # y_test = hf['y_test'][:,2160:2200]
    X_test = hf['X_test'][:, 6372:6480, :, :]
    y_test = hf['y_test'][:, 6372:6480]


y_test = np.asarray([y_test[:], np.abs(np.asarray(y_test[:], dtype=np.float32) - 1)]).T
y_test = np.squeeze(y_test, axis=1)
X_test =np.transpose(np.array(X_test), (1,0,2,3))
score_test, acc_test = model.evaluate(X_test, y_test, batch_size=20)
prob_pre = model.predict(X_test, batchSize, 1)


dot = model_to_dot(model, show_shapes=False, show_layer_names=True, rankdir='TB')
layers_by_depth = model.model.layers_by_depth
h=h5py.File('M2D-Motion.h5','w')
# h=h5py.File('M2D-NonMotion.h5','w')

modelDimension =[]
if X_test.ndim==4:
    modelDimension.append('2D')
    modelDimension=h.create_dataset('modelDimension',data=modelDimension)
elif X_test.ndim==5:
    modelDimension.append('3D')
    modelDimension=h.create_dataset('modelDimension', data=modelDimension)
else:
    print("the dimesnion should be 2D or 3D")



layer_by_depth=h.create_group('layer_by_depth')
weights=h.create_group('weights')
#allLayerNames=[]
maxCol = 0
maxRow = len(layers_by_depth)
# Save the structure,weights the layers' names in .h5 file
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
maxColu=h.create_dataset('maxCol',data=maxCol)
maxRowNumber=h.create_dataset('maxRow',data=maxRow)

# save the features
activation={}
act=h.create_group('activations')
for i,layer in enumerate(model.model.layers):
    get_activations = K.function([model.model.layers[0].input, K.learning_phase()], [layer.output, ])
    activation[layer.name]=get_activations([X_test[:], 0])[0]
    a = act.create_dataset(layer.name, data=activation[layer.name])

#output    = model.get_output()
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

# step_size = 0.019
# reg_param = 1/(2e-4)

step_size = 0.19
reg_param = 0.0000001

#data_c = test[100:110] # extract images from the examples as initial point
#resultAll = []
test=X_test[:]

data_c = test
oss_v = network_visualization.SubsetSelection(calcGrad, calcCost, data_c, alpha=reg_param, gamma=step_size)
result = oss_v.optimize(np.random.uniform(0, 1.0, size=data_c.shape))
result=result * test
result[result>0]=1
# result[result<0.2]=0

h.create_dataset('subset_selection', data=result)
h.close()

# fig=plt.figure()
# fig.suptitle('change gamma result')
#
# #result=np.squeeze(result,axis=1)
# nimgs = len(result)
# nrows = int(np.round(np.sqrt(nimgs)))
# ncols = int(nrows)
# if (nrows ** 2) <  nimgs:
#     ncols += 1
#
# fig=plot_subset_mosaic(result, nrows, ncols, fig)
# plt.show()
#
# fig2=plt.figure(2)
# fig2.suptitle('input')
#
# #result=np.squeeze(result,axis=1)
# nimgs = len(test)
# nrows = int(np.round(np.sqrt(nimgs)))
# ncols = int(nrows)
# if (nrows ** 2) <  nimgs:
#     ncols += 1
#
# fig2=plot_subset_mosaic(test, nrows, ncols, fig2)
# plt.show()
#
