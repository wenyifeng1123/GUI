# #coding:utf-8
import h5py
import os
import matplotlib.pyplot as plt
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


def pn(name):
    print name

(X_train, y_train), (X_test, y_test) = mnist.load_data()

# Only take a small part of the data to reduce computation time

X_train = X_train[:100]
y_train = y_train[:100]
X_test = X_test[:100]
y_test = y_test[:100]

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

# model.add(Dense(128))
# model.add(Activation('relu'))
# model.add(Dropout(0.5))

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

activations=[]


for i,layer in enumerate(model.layers):
    get_activations = K.function([model.layers[0].input, K.learning_phase()], [layer.output, ])
    activations.append(get_activations([X_test[:3], 0])[0])


h=h5py.File('layer.h5','w')
layers=h.create_group('layers')

for i,layer in enumerate(model.layers):
    ind=i
    i=layers.create_group(str(i))
    layer.name=i.create_group(layer.name)

    if len(layer.weights) == 0:
        weights=layer.name.create_dataset('weights',data=0)
        act=layer.name.create_dataset('activation',data=activations[ind])
        continue

    weights=layer.name.create_dataset('weights',data=layer.weights[0].container.data)
    act = layer.name.create_dataset('activation', data=activations[ind])


print(h.visit(pn))
#print(h['layers/0/conv2d_1/weights'].shape)

# very importent to close it !!!!!or the next time maybe cannot open it!!!!!!!!!!!!
h.close()

