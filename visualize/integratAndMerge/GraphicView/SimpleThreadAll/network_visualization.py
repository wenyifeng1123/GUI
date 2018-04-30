import theano
import theano.tensor as T
from scipy.optimize import fmin_l_bfgs_b
import proximal_alg
import keras.backend as K
from keras.utils.vis_utils import plot_model, model_to_dot
import numpy as np
import matplotlib.pyplot as plt
import h5py


def load_input_data(inputFile,test_min,test_max):
    hf=h5py.File(inputFile, 'r')
    X_test = hf['X_test'][:]
    y_test = hf['y_test'][:]
    y_test = np.asarray([y_test[:], np.abs(np.asarray(y_test[:], dtype=np.float32) - 1)]).T
    y_test = np.squeeze(y_test, axis=1)
    modelFormat=''


    if len(X_test.shape) == 4:
        X_test = np.transpose(np.array(X_test), (1, 0, 2, 3))
        X_test = X_test[test_min:test_max]
        y_test = y_test[test_min:test_max]
        modelFormat="2D"
        return X_test, y_test, modelFormat

    elif len(X_test.shape) == 5:
        X_test = np.transpose(np.array(X_test), (1, 0, 2, 3, 4))
        X_test = X_test[test_min:test_max]
        y_test = y_test[test_min:test_max]
        modelFormat = "3D"
        return X_test, y_test,modelFormat
    else:
        print("The dimension of the test data should be 4 ot 5")

def save_weights_activation_2D(model,h2, X_test):
    layers_by_depth = model.model.layers_by_depth
    h2 = h5py.File('test8080.h5', 'w')
    layer_by_depth = h2.create_group('layer_by_depth')

    weights = h2.create_group('weights')
    # allLayerNames=[]
    maxCol = 0
    maxRow = len(layers_by_depth)
    ## Save the structure,weights the layers' names in .h5 file
    for i in range(len(layers_by_depth)):
        i_layer = layer_by_depth.create_group(str(i))  # the No i layer  in the model
        for ind, layer in enumerate(layers_by_depth[i]):  # the layers in No i layer in the model
            if maxCol < ind:
                maxCow = ind
            i_ind = i_layer.create_group(str(ind))
            layer_name = i_ind.create_dataset('layer_name', data=layer.name)
            if len(layer.weights) == 0:
                w = 0
            else:
                w = layer.weights[0].container.data
            weights.create_dataset(layer.name, data=w)  # save the weights
            # allLayerNames.append(layer.name)
    maxColu = h2.create_dataset('maxCol', data=maxCol)
    maxRowNumber = h2.create_dataset('maxRow', data=maxRow)

    # save the features
    activation = {}
    act = h2.create_group('activations')
    for i, layer in enumerate(model.model.layers):
        get_activations = K.function([model.model.layers[0].input, K.learning_phase()], [layer.output, ])
        activation[layer.name] = get_activations([X_test, 0])[0]
        a = act.create_dataset(layer.name, data=activation[layer.name])

def save_weights_activation_3D(model,h3, X_test):
    layers_by_depth = model.model.layers_by_depth

def make_mosaic(im, nrows, ncols, border=1):
    import numpy.ma as ma

    nimgs = len(im)
    imshape = im[0].shape

    mosaic = ma.masked_all((nrows * imshape[0] + (nrows - 1) * border,
                            ncols * imshape[1] + (ncols - 1) * border),
                           dtype=np.float32)

    paddedh = imshape[0] + border
    paddedw = imshape[1] + border
    im
    for i in range(nimgs):
        row = int(np.floor(i / ncols))
        col = i % ncols

        mosaic[row * paddedh:row * paddedh + imshape[0],
        col * paddedw:col * paddedw + imshape[1]] = im[i]

    return mosaic

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

def plot_mosaic(im, nrows, ncols, fig, **kwargs):
    # Set default matplotlib parameters
    if not 'interpolation' in kwargs.keys():
        kwargs['interpolation'] = "none"

    if not 'cmap' in kwargs.keys():
        kwargs['cmap'] = "gray"

    nimgs = len(im)
    imshape = im[0].shape

    import matplotlib.pyplot as plt
    import numpy as np

    # ax = fig.add_subplot()

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

    fig.canvas.mpl_connect('button_press_event', on_click)

    return fig

def get_weights_mosaic(model, layer_id, n):
    """
    """

    # Get Keras layer
    layer = model.layers[layer_id]

    # Check if this layer has weight values
    if not hasattr(layer, "weights"):
        raise Exception("The layer {} of type {} does not have weights.".format(layer.name,
                                                                                layer.__class__.__name__))

    weights = layer.weights[0].container.data
    weights = np.transpose(weights, (3, 2, 0, 1))

    # For now we only handle Conv layer like with 4 dimensions
    if weights.ndim != 4:
        raise Exception("The layer {} has {} dimensions which is not supported.".format(layer.name, weights.ndim))

    # n define the maximum number of weights to display
    if weights.shape[0] < n:
        n = weights.shape[0]

    # mosaic = make_mosaic(weights[:n, 0], nrows, ncols, border=1)
    im = weights[:n, 0]

    return im

def plot_weights(model, layer_id, n, ax=None):
    """Plot the weights of a specific layer. ndim must be 4.
    """
    import matplotlib.pyplot as plt
    fig = plt.figure()

    layer = model.layers[layer_id]

    im = get_weights_mosaic(model, layer_id, n)

    # Create the mosaic of weights
    nrows = int(np.round(np.sqrt(n)))
    ncols = int(nrows)

    if nrows ** 2 < n:
        ncols += 1

    plt.suptitle("Layer #{} called '{}' of type {}".format(layer_id, layer.name, layer.__class__.__name__))

    fig = plot_mosaic(im, nrows, ncols, fig)
    fig.show()

    return fig

def plot_all_weights(model, n=64, **kwargs):
    import matplotlib.pyplot as plt
    from mpl_toolkits.axes_grid1 import make_axes_locatable

    # Set default matplotlib parameters
    if not 'interpolation' in kwargs.keys():
        kwargs['interpolation'] = "none"

    if not 'cmap' in kwargs.keys():
        kwargs['cmap'] = "gray"

    layers_to_show = []

    for i, layer in enumerate(model.layers[:]):
        if hasattr(layer, "weights"):
            if len(layer.weights) == 0:
                continue
            weights = layer.weights[0].container.data
            if weights.ndim == 4:
                layers_to_show.append((i, layer))

    n_mosaic = len(layers_to_show)
    # n_mosaic = len(model.layers)
    nrows = int(np.round(np.sqrt(n_mosaic)))
    ncols = int(nrows)

    if nrows ** 2 < n_mosaic:
        ncols += 1

    for i, (layer_id, layer) in enumerate(layers_to_show):
        fig = plot_weights(model, layer_id, n, ax=None)

        fig.suptitle("Layer #{} called '{}' of type {}".format(layer_id, layer.name, layer.__class__.__name__))

    return fig

def plot_feature_map(model, layer_id, X, n=256, ax=None, **kwargs):
    """
    """
    import keras.backend as K
    import matplotlib.pyplot as plt
    from mpl_toolkits.axes_grid1 import make_axes_locatable

    layer = model.layers[layer_id]

    try:
        get_activations = K.function([model.layers[0].input, K.learning_phase()], [layer.output, ])
        activations = get_activations([X, 0])[0]
    except:
        # Ugly catch, a cleaner logic is welcome here.
        raise Exception("This layer cannot be plotted.")

    # For now we only handle feature map with 4 dimensions
    if activations.ndim != 4:
        raise Exception("Feature map of '{}' has {} dimensions which is not supported.".format(layer.name,
                                                                                               activations.ndim))

    # Set default matplotlib parameters
    if not 'interpolation' in kwargs.keys():
        kwargs['interpolation'] = "none"

    if not 'cmap' in kwargs.keys():
        kwargs['cmap'] = "gray"

    fig = plt.figure(figsize=(15, 15))

    # Compute nrows and ncols for images
    n_mosaic = len(activations)
    nrows = int(np.round(np.sqrt(n_mosaic)))
    ncols = int(nrows)
    if (nrows ** 2) < n_mosaic:
        ncols += 1

    # Compute nrows and ncols for mosaics
    if activations[0].shape[0] < n:
        n = activations[0].shape[0]

    nrows_inside_mosaic = int(np.round(np.sqrt(n)))
    ncols_inside_mosaic = int(nrows_inside_mosaic)

    if nrows_inside_mosaic ** 2 < n:
        ncols_inside_mosaic += 1

    for i, feature_map in enumerate(activations):
        mosaic = make_mosaic(feature_map[:n], nrows_inside_mosaic, ncols_inside_mosaic, border=1)

        ax = fig.add_subplot(nrows, ncols, i + 1)

        im = ax.imshow(mosaic, **kwargs)
        ax.set_title("Feature map #{} \nof layer#{} \ncalled '{}' \nof type {} ".format(i, layer_id,
                                                                                        layer.name,
                                                                                        layer.__class__.__name__))

    fig.tight_layout()
    return fig

def plot_all_feature_maps(model, X, n=256, ax=None, **kwargs):
    figs = []

    for i, layer in enumerate(model.layers):

        try:
            fig = plot_feature_map(model, i, X, n=n, ax=ax, **kwargs)
        except:
            pass
        else:
            figs.append(fig)

    return figs

class Visualizer():

    def __init__(self, calcGrad, calcCost, input):
        """
        Visualizer for Deep Neural Networks. Solves an inverse problem to find a suited input
        that minimizes the cost function given in calcCost.

        Parameters:
        -----------
	  calcCost : function handle that computes the cost function for a given input
	  calcGrad : function handle that computes the gradient of the cost function
	  input : an input image (used for regularization or just to get the shape of the input)
        """
        self.calcGrad = calcGrad
        self.calcCost = calcCost
        self.input = np.asarray(input, dtype=np.float32)
        self.inp_shape = input.shape

    def optimize(self, x0, cost):
        return 0

    def map(self, x0):
        return self.optimize(x0, self.cost)


class DeepVisualizer(Visualizer):

    def __init__(self, calcGrad, calcCost, input, alpha=0.01):
        """
        Deep Visualization for Deep Neural Networks. Solves an inverse problem to find a suited input
        that minimizes the cost function given in calcCost.

        Parameters:
        -----------
	  calcCost : function handle that computes the cost function for a given input
	  calcGrad : function handle that computes the gradient of the cost function
	  input : an input image (used for regularization or just to get the shape of the input)
	  alpha : l2-regularization on the wanted input image to obtain feasible results
        """

        Visualizer.__init__(self, calcGrad, calcCost, input)

        self.alpha = alpha

    def costFun(self, x):
        """
        Function that computes the cost value for a given x

        Parameters:
        -----------
          x : input data
        """
        tmp = x.reshape(self.inp_shape)
        c = np.float64(self.calcCost(np.asarray(tmp, dtype=np.float32))) + self.alpha * np.dot(x.T, x)
        return c

    def gradFun(self, x):
        """
        Function that computes the gradient of the cost function at x

        Parameters:
        -----------
          x : input data
        """
        tmp = x.reshape(self.inp_shape)
        g = np.ravel(
            np.asarray(self.calcGrad(np.asarray(tmp, dtype=np.float32)), dtype=np.float64)) + 2 * self.alpha * x
        return g

    def optimize(self, x0):
        """
        Solves the inverse problem

        Parameters:
        -----------
	  x0 : initial solution
        """
        (result, f, d) = fmin_l_bfgs_b(lambda x: self.costFun(x), np.ravel(x0), lambda x: self.gradFun(x))
        print("optimization completed with cost: " + str(f))
        return result.reshape(self.inp_shape)


class SubsetSelection(Visualizer):

    def __init__(self, calcGrad, calcCost, input, alpha=0.01, gamma=0.1):
        """
        Subset selection for Deep Neural Networks. Solves an inverse problem to find a suited input
        that minimizes the cost function given in calcCost.

        Parameters:
        -----------
	  calcCost : function handle that computes the cost function for a given input
	  calcGrad : function handle that computes the gradient of the cost function
	  input : an input image (used for regularization or just to get the shape of the input)
	  alpha : l2-regularization on the wanted input image to obtain feasible results
	  gamma : step size for the proximal gradient algorithm
        """
        Visualizer.__init__(self, calcGrad, calcCost, input)
        self.alpha = alpha
        self.gamma = gamma

    def costFun(self, S, x):
        """
  Function that computes the cost value for a given x

  Parameters:
  -----------
    x : input data
  """
        return self.calcCost(S * x)

    def gradFun(self, S, x):
        """
  Function that computes the gradient of the cost function at x

  Parameters:
  -----------
    x : input data
  """
        return self.calcGrad(S * x) * x  # todo: sum over the dimensions of x which are not present in s!

    def optimize(self, x0, n_iter=50):
        """
        Solves the inverse problem

        Parameters:
        -----------
	  x0 : initial solution
	  n_iter : number of proximal gradient steps used for optimization
        """
        x0 = np.asarray(x0, dtype=np.float32)
        opt = proximal_alg.ProximalGradSolver(self.gamma, self.alpha, lambda x: self.costFun(x, self.input),
                                              lambda x: np.sum(np.abs(x)), lambda x: self.gradFun(x, self.input),
                                              proximal_alg.prox_l1_01)
        result = opt.minimize(x0, n_iter=n_iter)
        return result