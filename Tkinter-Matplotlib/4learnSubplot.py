from __future__ import print_function
'''
https://matplotlib.org/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots
'''
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2*np.pi, 400)
y = np.sin(x**2)

fig, ax = plt.subplots()
ax.plot(x, y)
ax.set_title('Simple plot')
#Creates two subplots and unpacks the output array immediately

f, (ax1, ax2) = plt.subplots(1, 2, sharey=True)
ax1.plot(x, y)
ax1.set_title('Sharing Y axis')
ax2.scatter(x, y)
#Creates four polar axes, and accesses them through the returned array

fig, axes = plt.subplots(2, 2, subplot_kw=dict(polar=True))
axes[0, 0].plot(x, y)
axes[1, 1].scatter(x, y)
#Share a X axis with each column of subplots

plt.subplots(2, 2, sharex='col')
#Share a Y axis with each row of subplots

plt.subplots(2, 2, sharey='row')
#Share both X and Y axes with all subplots

plt.subplots(2, 2, sharex='all', sharey='all')
#Note that this is the same as

plt.subplots(2, 2, sharex=True, sharey=True)
plt.show()