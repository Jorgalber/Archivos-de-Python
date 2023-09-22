# -*- coding: utf-8 -*-
"""
Created on Mon Sep  5 00:38:47 2022

@author: Jorge
"""
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np


def gf(x,y):
    suma = 0;
    prod = 1;
    suma = suma + (x**2*y**2)/4000;
    prod = prod * np.cos((x**2*y**2)/np.sqrt((x**2*y**2)+1));
    return suma - prod + 1;

plotN = 100
x = np.linspace(-30, 30, plotN)
y = np.linspace(-30, 30, plotN)
x, y = np.meshgrid(x,y)
z = gf(x,y)

fig = plt.figure()

axis = fig.gca( projection='3d')
axis.plot_surface(x, y, z, cmap='jet', shade= "false")
plt.show()
plt.contour(x,y,z)
plt.show()

fig = plt.figure()
ax = Axes3D(fig)
ax.plot_wireframe(x,y,z)