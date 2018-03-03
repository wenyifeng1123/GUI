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
from keras.models import load_model
from network_visualization import on_click,plot_mosaic,get_weights_mosaic,plot_weights,plot_all_weights,plot_feature_map,plot_all_feature_maps
import matplotlib.pyplot as plt

def on_click_axes(event):
    """Enlarge or restore the selected axis."""
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
                        border_mode='valid',activation="relu"))

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




# Plot all the weights when possible of the model
# The maximum number of filters per layer is n=256
# _ = plot_all_weights(model, n=256)

# Plot all the feature maps of the layer 2
# The maximum number of filters per feature maps is n=9

#_ = plot_feature_map(model, 1, X_test[:3], n=3)
#_ = plot_all_feature_maps(model, X_test[:9], n=9)
#plt.show()

layerLength = len(model.layers)
fig1 = plt.figure()
fig1.show()
axNumber = layerLength*2-1



for i in range(axNumber):
    ax = fig1.add_subplot(axNumber,1,i+1)
    if i%2==0:
        bbox_props = dict(boxstyle="round", fc="w", ec="0.5", alpha=0.9)
        ax.text(0.5, 0.5, model.layers[int(i/2)].name, ha="center", va="center", size=20,
                bbox=bbox_props)
        ax.name=model.layers[int(i/2)].name

    elif i!=axNumber-1:
        ax.annotate('', xy=(0.5,0), xytext=(0.5,1),
                    arrowprops=dict(facecolor='black', shrink=0.05))
        ax.name='arrow'
    else:
        pass

    ax.set_axis_off()

fig1.canvas.mpl_connect('button_press_event', on_click_axes)
plt.show()

