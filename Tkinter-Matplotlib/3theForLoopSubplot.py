# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt

plt.figure(1)

for row in range(0,4):
    for col in range(0,8):
        plt.subplot2grid((4, 8), (row, col))
        plt.plot([1, 2], [1, 4])


plt.show()