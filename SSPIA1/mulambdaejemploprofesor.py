# -*- coding: utf-8 -*-
"""
Created on Tue Sep 27 16:04:10 2022

@author: Jorge
"""

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

def f(x,y):
  return x*np.exp(-x**2-y**2)

plotN = 200
x = np.linspace(-2,2, plotN)
y = np.linspace(-2,2, plotN)

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

def recombinacion(xp,xm):
  return .5 * xp+xm

import random
import copy

iter = range(1,300) # numero de iteracions--- generaciones

mu = 30 #cantidad de individuos
dimension = 2
lam=100

x_lower = np.array([-5 , -5]) # cota minima
x_upper = np.array([5, 5])   #cota maxima

g = np.zeros(len(iter))

#inicializar vectores sigma, fitness, individuos
x_test = np.zeros((mu+1,dimension))
sigma = np.zeros((mu+1,dimension))
fitness = np.zeros((mu+1,2))
index = np.zeros((mu+1,1))

#inicializar poblacion
for i in range(0,mu):
  x_test[i,:] = x_lower + (x_upper - x_lower)*np.array([random.random(), random.random()])
  sigma[i,:] = .2*np.array([random.random(),random.random()])
  fitness[i,:] = np.array([f(x_test[i,0],x_test[i,1]),i])

#iterar algoritmo
for i in range(lam):
  for j in iter:
    r1 =  random.randint(0,mu)
    r2 = copy.copy(r1)

    while r1==r2:
      r2= random.randint(0,mu)

    x_test[mu,:] = recombinacion(x_test[r1,:],x_test[r2,:])
    sigma[mu,:] = recombinacion(sigma[r1,:],sigma[r2,:])


    r = np.random.normal(0, sigma[mu,:],2)
    x_test[mu,:] = x_test[mu,:] + r
    fitness[mu,0] = f(x_test[mu,0],x_test[mu,1])


    #eliminar el peor individuo
    I = np.arange(0,mu+1)
    fitness[:,1] = I
    ordenados = sorted(fitness, key=lambda fit : fit[0])
    
    for i in range(0,mu):
      index[i] = ordenados[i][1]
    

    #extraer los indices de los indviduos ordenados 
    p = index.T.flatten()  
    p= [int(x) for x in p]
    print(p)

  # acomodar los mejores individuos al principio y el peor al final
    x_test = x_test[p,:];
    sigma = sigma[p,:];
    fitness = fitness[p,:];
  # fin eliminar el peor individuo
  
  ordenados = sorted(fitness, key=lambda fit : fit[0])

mejor = int(ordenados[0][1])

print(x_test[mejor,:])

print("valores que optimizan la función =",x_test[mejor,0],x_test[mejor,1])
print("minimo en =", f(x_test[mejor,0],x_test[mejor,1] ))