# -*- coding: utf-8 -*-
"""
Created on Tue Aug 16 13:55:12 2022

@author: Jorge
"""

import matplotlib.pyplot as plt;
import numpy as np;

def f(x):
  return x**4 + 5*x**3 + 4*x**2 -4*x + 1

def df(x):
  return 4*x**3 + 15*x**2 + 8*x - 4

def ddf(x):
  return 12*x**2 + 30*x + 8

x=np.arange(-4,1,0.2)
y=[f(i) for i in x]

plt.plot(x,y,linewidth=3, color=(0.2,0.1,0.4))

plt.grid()
plt.axis("equal")
plt.xlabel("x")
plt.ylabel("F(X)")
plt.title('Lab DLS')

x1 = -2.96
x2 = -1.10
x3 = 0.31

y1 = f(x1)
y2 = f(x2)
y3 = f(x3)

print(x1,",",y1)
print(x2,",",y2)
print(x3,",",y3)

plt.plot(x,y,linewidth=3,color=(0.2,0.1,0.4))
plt.plot(x1,y1, 'o', color = ("red"))
plt.plot(x2,y2, 'o', color = ("red"))
plt.plot(x3,y3, 'o', color = ("red"))
plt.show()

x1 = -2.96
x2 = -1.10
x3 = .31

y1 = ddf(x1)
y2 = ddf(x2)
y3 = ddf(x3)

print(y1)
print(y2)
print(y3)