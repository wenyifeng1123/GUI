import matplotlib.pyplot as plt




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

fig, axes = plt.subplots(nrows=2, ncols=2)
for ax, color in zip(axes.flat, ['r', 'g', 'b', 'c']):
    ax.plot(range(10), color=color)
fig.canvas.mpl_connect('button_press_event', on_click)
plt.show()
