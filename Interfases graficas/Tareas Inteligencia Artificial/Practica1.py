# -*- coding: utf-8 -*-
"""
Created on Thu Feb  3 22:30:59 2022

@author: Jorge
"""

import matplotlib
from tkinter import *;
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import tkinter as tk
import numpy as np

window=tk.Tk()
window.title("Practica 1")
window.iconbitmap("icono.ico");

padding=20;
coords = []
lx1=[]
lx2=[]
v=[]
temp=[]

def onclick(event):
    global ix1, ix2
    ix1, ix2 =event.xdata, event.ydata
    print('button=%d, x=%d, y=%d, xdata=%f, ydata=%f' %(event.button, event.x, event.y, event.xdata, event.ydata));
    ax.plot(event.xdata, event.ydata, 'Pk');
    global coords
    coords.append((ix1, ix2))
    fig.canvas.draw();


def getEntry():
    w1=float(cuadroW1.get());
    w2=float(cuadroW2.get());
    oO=float(cuadroO.get());
    a=(-w1)/w2;
    b=oO/w2;
    if(w1=="")or(w2=="")or(oO=="")or (coords==[]):
        pass
    else:
        global lx1,lx2
        xmin, xmax = -10,10
        t=np.arange(xmin, xmax, 0.1)
        lx1=[x[0]*w1 for x in coords];
        lx2=[x[1]*w2 for x in coords];
        for i in range(len(lx1)):
            v.append((lx1[i]+lx2[i])-oO)
        for i in v:
            if  i>=1:
                temp.append(v.index(i));
        for i in temp:
            ax.plot(lx1[i], lx2[i], 'Pb');
        ax.plot(t, a * t + b ,"r" )
        canvas.draw()
        
def limpiarGraf():
    ax.cla();
    coords.clear();
    lx1.clear();
    lx2.clear();
    v.clear();
    temp.clear()
    ax.set_xlim(-10,10);
    ax.set_ylim(-10,10);
    ax.grid();
    canvas.draw();
    cuadroW1.delete(0,"end");
    cuadroW1.insert(0,"");
    cuadroW2.delete(0,"end");
    cuadroW2.insert(0,"");
    cuadroO.delete(0,"end");
    cuadroO.insert(0,"");

fig=Figure(figsize=(5,5));
ax=fig.add_subplot(111);
ax.set_xlim(-10,10);
ax.set_ylim(-10,10);
ax.grid()

canvas = FigureCanvasTkAgg(fig, master=window);
canvas.get_tk_widget().grid(row=1,column=0, rowspan=4);

W1Label=Label(text="W1:");
W1Label.grid(row=1,column=1);
cuadroW1=Entry();
cuadroW1.grid(row=1,column=2,padx=padding,pady=padding,columnspan=2);

W2Label=Label(text="W2:");
W2Label.grid(row=2,column=1);
cuadroW2=Entry();
cuadroW2.grid(row=2,column=2,padx=padding,pady=padding,columnspan=2);

OLabel=Label(text="Θ:");
OLabel.grid(row=3,column=1);
cuadroO=Entry();
cuadroO.grid(row=3,column=2,padx=padding,pady=padding,columnspan=2);

botonEnvio=Button(text="Iniciar", command=lambda:getEntry());
botonEnvio.grid(row=4,column=2,padx=padding,pady=padding);

botonlim=Button(text="Limpiar", command=lambda:limpiarGraf());
botonlim.grid(row=4,column=3,padx=padding,pady=padding);

canvas.mpl_connect('button_press_event', onclick)
window.mainloop()