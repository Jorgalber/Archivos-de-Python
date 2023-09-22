# -*- coding: utf-8 -*-
"""
Created on Tue Aug 30 21:00:55 2022

@author: Jorge
"""

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

def f(x,y):
  return x*np.exp((-x**2)*(-y**2))

def g1(x,y):
  return (-(2*(x**2))-1)*np.exp((-x**2)*(-y**2))

def g2(x,y):
  return -2*(x*y*np.exp((-x**2)*(-y**2)))

plotN = 200
x = np.linspace(-20,20, plotN)
y = np.linspace(-20,20, plotN)

x, y = np.meshgrid(x,y)

z = f(x,y)

fig = plt.figure()

axis = fig.gca( projection='3d')
axis.plot_surface(x, y, z, cmap='jet', shade= "false")
plt.show()
plt.contour(x,y,z)
plt.show()

fig = plt.figure()
ax = Axes3D(fig)
ax.plot_wireframe(x,y,z)

#gradiente

n = range(1,10)
x0 = 2
y0 = -2
h = .5

for i in n:
  x0 -= h*g1(x0)
  y0 -= h*g2(y0)
  

fig = plt.figure()
ax = Axes3D(fig)
ax.plot_wireframe(x,y,z)
print("valores que optimizan la función =",x0, y0)
print("minimo en =", f(x0,y0))