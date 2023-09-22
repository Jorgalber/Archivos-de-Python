# -*- coding: utf-8 -*-
"""
Created on Tue Aug 16 21:12:24 2022

@author: Jorge
"""

import matplotlib.pyplot as plt;
import numpy as np;

def f(x):
  return x**3

def df(x):
  return 3*x**2

def ddf(x):
  return  6*x

x=np.arange(-2,2,0.1)
y=[f(i) for i in x]

plt.plot(x,y,linewidth=2, color=(0.2,0.1,0.4))
plt.grid()
plt.axis("equal")
plt.xlabel("x")
plt.ylabel("f(X)")

x1=0
y1=f(x1)

plt.plot(x1,y1, 'o', color = ("red"))


