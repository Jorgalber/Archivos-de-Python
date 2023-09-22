# -*- coding: utf-8 -*-
"""
Created on Tue Feb  8 13:45:34 2022

@author: Jorge
"""

import matplotlib
from tkinter import filedialog
from tkinter.filedialog import askopenfilename
from tkinter import *;
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import tkinter as tk
import numpy as np
import pandas as pd
import random

window=tk.Tk()
window.title("Ejercicio 1")
window.iconbitmap("icono.ico");

padding=20;
x1=[]
x2=[]

y=[]
r = random.random()
azul = random.random()
g = random.random()
color = (r, g, azul)
dataset=[]
fichero=""
m=[];
b=-0.5;


def abrir():
    fichero=filedialog.askopenfilenames(title="Abrir", initialdir="C:",filetypes=(("Ficheros de CSV","*.csv"),
                                                                                  ("Todos los archivos","*.*")));
    dataset = pd.read_csv(fichero[0], header=None)
    x1=dataset.iloc[:,0].values
    x2=dataset.iloc[:,1].values
    Y=dataset.iloc[:,2].values
    for i in x1,x2:
        ax.scatter(x1, x2, color=color);
    fig.canvas.draw();
        
def getEntry():
    crit=float(cuadroCF.get());
    epo=float(cuadroEp.get());
    taza=float(cuadrotaza.get());
    meanX1=np.mean(x1);
    meanX2=np.mean(x2);
    sigmax1=np.std(x1);
    sigmax2=np.std(x2);
    m=[len(x1)*len(x2)]  
    iteracin=1;
    w1=0.2;
    w2=0.5;
    b=-0.5;
    v=[]
    while iteracin<=epo:
        for i in m:
            v.append=(((x1[i]*w1)+(x2[i]*w2))+b)
            if v[i]>0:
                y[i]=1;
            else:
                y[i]=0;
            if ((Y[i]-y[i])!=0):
                w1=w1+((taza*x1[i]))
                w2=w2+((taza*x2[i]))
                b=b+taza;
            iteracin += 1
                        
def limpiarGraf():
    ax.cla();
    x1.clear();
    x2.clear();
    y.clear();
    dataset.clear()
    ax.grid();
    fichero=""
    fig.canvas.draw();

fig=Figure(figsize=(5,5));
ax=fig.add_subplot(111);
ax.grid();

canvas = FigureCanvasTkAgg(fig, master=window);
canvas.get_tk_widget().grid(row=1,column=0,columnspan=2, rowspan=3);

CFLabel=Label(text="Criterio Finalización:");
CFLabel.grid(row=1,column=2);
cuadroCF=Entry();
cuadroCF.grid(row=1,column=3,padx=padding,pady=padding,columnspan=2);

epLabel=Label(text="Épocas:");
epLabel.grid(row=2,column=2);
cuadroEp=Entry();
cuadroEp.grid(row=2,column=3,padx=padding,pady=padding,columnspan=2);

tazaLabel=Label(text="Taza:");
tazaLabel.grid(row=3,column=2);
cuadrotaza=Entry();
cuadrotaza.grid(row=3,column=3,padx=padding,pady=padding,columnspan=2);

botonEnvio=Button(text="Iniciar", command=lambda:getEntry());
botonEnvio.grid(row=4,column=0,padx=padding,pady=padding);

botonlim=Button(text="Limpiar", command=lambda:limpiarGraf());
botonlim.grid(row=4,column=1,padx=padding,pady=padding);

BotonAbrir=Button(text="Abrir fichero", command=lambda:abrir());
BotonAbrir.grid(row=0,column=0,padx=padding,pady=padding,columnspan=2);

window.mainloop()