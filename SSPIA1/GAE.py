# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 15:33:48 2022

@author: Jorge
"""

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
import random
import copy

def f(x,y):
  return (x-2)**2 + (y-2)**2

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

def aptitud_i(x_i):
  aptitud = np.zeros(len(x_i))
  for i in range(len(x_i)):
    if f(x_i[i,0],x_i[i,1])>=0:
      aptitud[i] =  1/(1+f(x_i[i,0],x_i[i,1]))
    else:
      aptitud[i] = 1+ abs(f(x_i[i,0],x_i[i,1]))
  return aptitud

def ruleta(aptitud):
    pi = np.zeros(len(aptitud))
    for i in range(len(aptitud)):
      pi[i] = aptitud[i]/sum(aptitud)
    return pi

def seleccion(aptitud):
  r = random.uniform(0,1)
  p_sum = 0
  pi = ruleta(aptitud)
  for i in range(len(aptitud)):
    p_sum = p_sum + pi[i]
    if p_sum >= r:
      n = i
      return n
  n = len(x_i)
  return n

def cruza(xp,xm):
  pc = random.randint(0,dimension-1)
  y1 = copy.copy(xp) 
  y2 = copy.copy(xm) 

  y1[pc:] = copy.copy(xm[pc:]) 
  y2[pc:] = copy.copy(xp[pc:]) 
  return [y1,y2]

def mutacion(y):
  for i in range(len(y)):
    for j in range(dimension-1):
      if random.uniform(0,1)<pm:
        y[i,j] = x_lower[j] + (x_upper[j] - x_lower[j])*random.uniform(0,1)
  return y

def elite(population, aptitud):
    
    
#Algoritmo genetico

iter = range(1,300) # numero de iteracions--- generaciones

dimension = 2

x_lower = np.array([-5 , -5]) # cota minima
x_upper = np.array([5, 5])   #cota maxima

g = np.zeros(len(iter))

pm = 0.7

##generar poblacion inicial
population= 50
#x_i = np.zeros((len(iter),dimension)) #poblacion inicial
x_i = np.zeros((population,2))
for i in range(0,population):
  x_i[i,:] = x_lower + (x_upper - x_lower)*np.array([random.uniform(0,1), random.uniform(0,1)])


##iterar GA

for i in iter:
  aptitud = aptitud_i(x_i)

  y =  np.zeros((population,dimension))

  for i in range(0,population,2):
    r1 = seleccion(aptitud)
    r2 = seleccion(aptitud)

    while r2==r1:
      r2 = seleccion(aptitud)

    [y1,y2]=cruza(x_i[r1,:],x_i[r2,:])
    y[i,:] = y1
    y[i+1,:] = y2

  y = mutacion(y)
  x_i = copy.copy(y)


aptitud = aptitud_i(x_i)
mejor = max(aptitud)
index = np.where(aptitud == mejor)
#print(index) 

#print(x_i[index,0],x_i[index,1])
#print(f(x_i[index,0],x_i[index,1]))
#print(len(y))

print("valores que optimizan la función =",x_i[index,0],x_i[index,1])
print("minimo en =", f(x_i[index,0],x_i[index,1]))

g1 = np.zeros((dimension,len(iter)))
print(x_i[0,1])
print(f(x_i[0,0],x_i[0,1]))
#print(x_i)
print(aptitud_i(x_i))
prueba = cruza(x_i[1,:],x_i[2,:])
print(prueba[1])