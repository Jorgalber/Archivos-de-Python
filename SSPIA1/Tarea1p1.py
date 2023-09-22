# -*- coding: utf-8 -*-
"""
Created on Tue Aug 16 20:03:25 2022

@author: Jorge
"""

import matplotlib.pyplot as plt;
import numpy as np;


def f(x):
  return (x**2)*np.exp(-x**2) 

def df(x):
  return 2*(np.exp(-x**2)*x-2*(np.exp(-x**2))*x**3)

def ddf(x):
  return (4*np.exp(-x**2)*(x**4))-(10*np.exp(-x**2)*(x**2))+(2*np.exp(-x**2))

x=np.arange(-2,2,0.1)
y=[f(i) for i in x]

plt.plot(x,y,linewidth=2, color=(0.2,0.1,0.4))
plt.grid()
plt.axis('equal')
plt.xlabel("x")
plt.ylabel("f(X)")
#Maximos y minimos locales 
x1=-1
x2=0
x3=1
y1=f(x1)
y2=f(x2)
y3=f(x3)
plt.plot(x1,y1, 'o', color = ("red"))
plt.plot(x2,y2, 'o', color = ("red"))
plt.plot(x3,y3, 'o', color = ("red"))

