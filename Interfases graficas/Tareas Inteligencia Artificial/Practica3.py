# -*- coding: utf-8 -*-
"""
Created on Mon Feb 28 19:38:07 2022

@author: Jorge
"""

import matplotlib
from tkinter import *;
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import tkinter as tk
import numpy as np
import math as mt

window=tk.Tk()
window.title("Practica 2")
window.iconbitmap("icono.ico");

padding=10;
coords = [];
lx1=[];
lx2=[];
lydes=[];
lyoptenida=[];
temp=[];
gradiente=[];
varOpc=IntVar();
error=[]
x1=[]
x2=[]
v=[]

def onclick(event):
    global ix1, ix2
    global coords
    ix1, ix2 =event.xdata, event.ydata;
    print('button=%d, x=%d, y=%d, xdata=%f, ydata=%f' %(event.button, event.x, event.y, event.xdata, event.ydata));
    if varOpc.get()==1:
        if event.button==1:
            ax.plot(event.xdata, event.ydata, 'Pr');
            coords.append((ix1,ix2,-1))
        else:
            ax.plot(event.xdata, event.ydata, 'Pb');
            coords.append((ix1,ix2,1))
    if varOpc.get()==2:
        if event.button==1:
            ax.plot(event.xdata, event.ydata, 'Pr');
            coords.append((ix1,ix2,-1))
        else:
            ax.plot(event.xdata, event.ydata, 'Pb');
            coords.append((ix1,ix2,1))
    if varOpc.get()==3:
        if event.button==1:
            ax.plot(event.xdata, event.ydata, 'Pr');
            coords.append((ix1,ix2,0))
        else:
            ax.plot(event.xdata, event.ydata, 'Pb');
            coords.append((ix1,ix2,1))
    fig.canvas.draw();

def getEntry():
    w1=0.3;
    w2=0.4;
    theta=0.1;
    eta=float(cuadroEta.get());
    a=1;
    b=0.5;
    iteracion=100;
    inicio=1
    if(eta=="")or(coords==[]):
        pass
    else:
        global lx1,lx2,lydes,lyoptenida,error,x1,x2;
        x1=[x[0] for x in coords];
        x2=[x[1] for x in coords];
        x1.append(1);
        x2.append(theta);
        while inicio<=iteracion:
            lx1=[x*w1 for x in x1];
            lx2=[x*w2 for x in x2];
            lydes=[x[2] for x in coords];
            for i in range(len(lx1)):
                v=((lx1[i]+lx2[i])-theta);
            #for i in v:
                lyoptenida=v;
            for i in (lydes):
                errores=(lydes[i]-lyoptenida)
                #temp.append((lydes[i]-lyoptenida[i]));
                #error.append(1/len(coords)*temp[i])
            if (errores!=0):
                #w1=w1+eta*(temp[i])*np.exp(temp[i]);
                #w2=w2+eta*(temp[i])*np.exp(temp[i]);
                w1=w1+eta*((x1[i]*x2[i])*(errores));
                w2=w2+eta*(errores);
                b=b+a*errores;
                #tanh
                if varOpc.get()==1:
                    t1=np.linspace(-len(x1)*2,len(x1)*2,100)
                    t2=np.tanh((errores))*t1
                    #t2=np.tanh((w1* t1 + b) / (-w2))
                    if inicio!= iteracion:
                        ax.plot(t1,t2,"y")
                        fig.canvas.draw();
                    else:
                        ax.plot(t1,t2,"b")
                        fig.canvas.draw();
                    #lineal
                if varOpc.get()==2:
                    t1=np.arange(-len(x1)*2,len(x1)*2,0.1)
                    t2=(a*errores)*t1
                    if inicio!=iteracion:
                        ax.plot(t1,t2,"y")
                        fig.canvas.draw();
                    else:
                        ax.plot(t1,t2,"b")
                        fig.canvas.draw();
                    #Sigmoide
                if varOpc.get()==3:
                    t1=np.arange(-len(x1)*2,len(x1)*2,0.2)
                    t2=(1/(1+np.exp(-errores)**(-a*errores)))*t1
                    if inicio!= iteracion:
                        ax.plot(t1,t2,"y")
                        fig.canvas.draw();
                    else:
                        ax.plot(t1,t2,"b")
                        fig.canvas.draw();
                print("Iteracion:",inicio,"Nuevo W1:",w1,"Nuevo W2:",w2,"Nuevo b:",b);
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
    #lyoptenida.clear();
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
canvas.get_tk_widget().grid(row=1,column=0, rowspan=8);

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
OInitialLabel=Label(text="0.1");
OInitialLabel.grid(row=3,column=2);

EtaLabel=Label(text="η:");
EtaLabel.grid(row=4,column=1,padx=padding,pady=padding);
cuadroEta=Entry();
cuadroEta.grid(row=4,column=2,padx=padding,pady=padding,columnspan=2);

Radiobutton(text="Tangente Hiperbólica",variable=varOpc, value=1).grid(row=5,column=2);
Radiobutton(text="Lineal",variable=varOpc, value=2).grid(row=6,column=2);
Radiobutton(text="Logística",variable=varOpc, value=3).grid(row=7,column=2);

varOpc.set(1)

botonEnvio=Button(text="Iniciar", command=lambda:getEntry());
botonEnvio.grid(row=8,column=2,padx=padding,pady=padding);

botonlim=Button(text="Limpiar", command=lambda:limpiarGraf());
botonlim.grid(row=8,column=3,padx=padding,pady=padding);

canvas.mpl_connect('button_press_event', onclick)
window.mainloop()