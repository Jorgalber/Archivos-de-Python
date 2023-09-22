# -*- coding: utf-8 -*-
"""
Created on Wed Feb 23 13:38:38 2022

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
window.title("Practica 2")
window.iconbitmap("icono.ico");

padding=10;
coords = [];
lx1=[];
lx2=[];
lydes=[];
lyoptenida=[];
v=[];
temp=[];

def onclick(event):
    global ix1, ix2
    global coords
    ix1, ix2 =event.xdata, event.ydata;
    print('button=%d, x=%d, y=%d, xdata=%f, ydata=%f' %(event.button, event.x, event.y, event.xdata, event.ydata));
    if event.button==1:
        ax.plot(event.xdata, event.ydata, 'Pr');
        coords.append((ix1,ix2,1))
    else:
        ax.plot(event.xdata, event.ydata, 'Pb');
        coords.append((ix1,ix2,-1))
    fig.canvas.draw();


def getEntry():
    w1=0.3;
    w2=0.4;
    theta=0.4;
    eta=float(cuadroEta.get());
    a=1;
    b=0.5;
    iteracion=100;
    inicio=1
    if(eta=="")or(coords==[]):
        pass
    else:
        while inicio<iteracion:
            global lx1,lx2,lydes,lyoptenida,gradiente;
            lx1=[x[0]*w1 for x in coords];
            lx2=[x[1]*w2 for x in coords];
            lydes=[x[2] for x in coords];
            for i in range(len(lx1)):
                v.append((lx1[i]+lx2[i]+theta)-theta);
            for i in v:
                if i>0:
                    lyoptenida.append(1);
                else:
                    lyoptenida.append(0);
            for i in range(len(lydes)):
                temp.append(lydes[i]-lyoptenida[i]);
                if (temp[i]!=0):
                    gradiente=2*(temp[i])
                    w1=w1+eta*(temp[i])*lx1[i];
                    w2=w2+eta*(temp[i])*lx2[i];
                    b = b + a *temp[i];
                print("Iteracion:",inicio,"Nuevo W1:",w1,"Nuevo W2:",w2,"Nuevo b:",b);
                t1 = np.arange(-10, 10, 0.1)
                t2 = (w1* t1 + b) / (-w2)
                ax.plot(t1,t2,"g")
                fig.canvas.draw();
                W1InitialLabel.config(text=w1)
                W2InitialLabel.config(text=w2)
                OInitialLabel.config(text=theta)
                inicio+=1;
   
def limpiarGraf():
    ax.cla();
    coords.clear();
    lx1.clear();
    lx2.clear();
    lydes.clear();
    lyoptenida.clear();
    v.clear();
    temp.clear()
    ax.set_xlim(-10,10);
    ax.set_ylim(-10,10);
    ax.grid();
    canvas.draw();
    cuadroEta.delete(0,"end");
    cuadroEta.insert(0,"");

fig=Figure(figsize=(5,5));
ax=fig.add_subplot(111);
ax.set_xlim(-10,10);
ax.set_ylim(-10,10);
ax.grid()

canvas = FigureCanvasTkAgg(fig, master=window);
canvas.get_tk_widget().grid(row=1,column=0, rowspan=4);

W1Label=Label(text="W1:");
W1Label.grid(row=1,column=1,padx=padding,pady=padding);
W1InitialLabel=Label(text="0.3");
W1InitialLabel.grid(row=1,column=2);

W2Label=Label(text="W2:");
W2Label.grid(row=2,column=1,padx=padding,pady=padding);
W2InitialLabel=Label(text="0.4");
W2InitialLabel.grid(row=2,column=2);

OLabel=Label(text="Θ:");
OLabel.grid(row=3,column=1,padx=padding,pady=padding);
OInitialLabel=Label(text="0.4");
OInitialLabel.grid(row=3,column=2);

EtaLabel=Label(text="η:");
EtaLabel.grid(row=4,column=1,padx=padding,pady=padding);
cuadroEta=Entry();
cuadroEta.grid(row=4,column=2,padx=padding,pady=padding,columnspan=2);

botonEnvio=Button(text="Iniciar", command=lambda:getEntry());
botonEnvio.grid(row=5,column=2,padx=padding,pady=padding);

botonlim=Button(text="Limpiar", command=lambda:limpiarGraf());
botonlim.grid(row=5,column=3,padx=padding,pady=padding);

canvas.mpl_connect('button_press_event', onclick)
window.mainloop()