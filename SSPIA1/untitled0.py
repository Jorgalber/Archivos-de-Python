# -*- coding: utf-8 -*-
"""
Created on Sun Sep  4 22:34:19 2022

@author: Jorge
"""

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

def griewank_function(x, y):
    suma = 0
    prom = 1
    suma +=(x**2 + y**2)/4000
    prom *= np.cos(x/np.sqrt(x+1))
    return suma - prom + 1


plotN = 100
x = np.linspace(-40, 40, plotN)
y = np.linspace(-40, 40, plotN)

x, y = np.meshgrid(x,y)

z = griewank_function(x,y)

fig = plt.figure()

axis = fig.gca( projection='3d')
axis.plot_surface(x, y, z, cmap='jet', shade= "false")
plt.show()
plt.contour(x,y,z)
plt.show()

fig = plt.figure()
ax = Axes3D(fig)
ax.plot_wireframe(x,y,z)