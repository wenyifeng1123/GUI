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
# model=load_model('testout4040_lr_0.0005_bs_128_model.h5')
# plot_model(model,'M2D.png',show_shapes='false')



with h5py.File('crossVal4040.h5','r') as hf:
    X_test = hf['X_test'][:,2052:2160,:,:]
    # y_test = hf['y_test'][:,6372:6480]
    # X_test = hf['X_test'][:,2052:2160, :, :]
    # y_test = hf['y_test'][:,2052:2160]


# y_test = np.asarray([y_test[:], np.abs(np.asarray(y_test[:], dtype=np.float32) - 1)]).T
# y_test = np.squeeze(y_test, axis=1)
X_test =np.transpose(np.array(X_test), (1,0,2,3))
# y_test2 = np.asarray([y_test[:], np.abs(np.asarray(y_test[:], dtype=np.float32) - 1)]).T
# y_test2 = np.squeeze(y_test, axis=1)
# X_test2 =np.transpose(np.array(X_test), (1,0,2,3))


# class_idx = 0
# reg_param = 1 / (2e-4)
# output =T.dmatrix('output')
# output=model.output
# input = model.input
# cost  = -T.sum(T.log(input[:,class_idx]+1e-8))
# gradient = theano.tensor.grad(cost, input)
# calcCost = theano.function([input], cost)
# calcGrad = theano.function([input], gradient)
#
# #2. Use subset selection:
#
#
#
# step_size = 0.19
# reg_param = 0.0000001
#
# test=X_test[:]
#
# data_c = test
# oss_v = network_visualization.SubsetSelection(calcGrad, calcCost, data_c, alpha=reg_param, gamma=step_size)
# result = oss_v.optimize(np.random.uniform(0, 1.0, size=data_c.shape))
# result=result * test
# result[result>0]=1


fig=plt.figure()
fig.suptitle('input')

#result=np.squeeze(result,axis=1)
nimgs = len(X_test)
nrows = int(np.round(np.sqrt(nimgs)))
ncols = int(nrows)
if (nrows ** 2) <  nimgs:
    ncols += 1

fig=plot_subset_mosaic(X_test, nrows, ncols, fig)
plt.show()

# fig2=plt.figure()
# fig2.suptitle('input motion')

# #result=np.squeeze(result,axis=1)
# nimgs = len(X_test2)
# nrows = int(np.round(np.sqrt(nimgs)))
# ncols = int(nrows)
# if (nrows ** 2) <  nimgs:
#     ncols += 1
#
# fig2=plot_subset_mosaic(X_test2, nrows, ncols, fig2)
# plt.show()

