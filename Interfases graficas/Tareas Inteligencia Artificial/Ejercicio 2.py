# -*- coding: utf-8 -*-
"""
Created on Mon Feb 14 15:54:03 2022

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

x1=[];
x2=[];
x3=[];
Y=[];


dataset=[];
fichero="";

temp=[]
padding=10;
coordsx1 = [];
coordsx2 = [];
coordsx3=[];
lx1=[];
lx2=[];
lx3=[];
lydes=[];
lyoptenida=[];
v=[];
temp=[];

def abrir():
    global x1,x2,x3,Y,lydes,train,test,parti,particion
    entrena=float(cuadroEntrena.get())
    parti=float(cuadroParticiones.get())
    if(entrena=="")or(parti==""):
        pass
    else:
        
        fichero=filedialog.askopenfilenames(title="Abrir", initialdir="C:",filetypes=(("Ficheros de CSV","*.csv"),
                                                                                      ("Todos los archivos","*.*")));
        dataset = pd.read_csv(fichero[0],header=None)
        particion=dataset[:int((len(dataset))/parti)]
        train=particion[:int((len(particion))*entrena)]
        test = particion[int((len(particion))*entrena):]
        x1=train.iloc[:,0].values
        x2=train.iloc[:,1].values
        x3=train.iloc[:,2].values
        Y=train.iloc[:,3].values
        for i in Y:
            lydes.append(i)
        for ix1 in x1:
            coordsx1.append((ix1))
        for ix2 in x2:
            coordsx2.append(ix2)
        for ix3 in x2:
            coordsx3.append(ix3)
        ax.plot(x1, x2, x3, 'Pk');
        fig.canvas.draw();


def getEntry():
    crit=float(cuadroCF.get());
    epo=float(cuadroEp.get());
    tasa=float(cuadrotaza.get());
    w1=0.5;
    w2=0.5;
    w3=0.5;
    b=0.5;
    a=1;
    itera=0;
    global lx1,lx2,lydes,lyoptenida;
    if(crit=="")or(epo=="")or(tasa=="")or(coordsx1==[])or(coordsx2==[])or(lydes==[]):
        pass
    else:
        while itera<=epo:
            lx1=[x*w1 for x in coordsx1];
            lx2=[x*w2 for x in coordsx2];
            lx3=[x*w3 for x in coordsx3];
            for i in range(len(lx1)):
                v.append((lx1[i]+lx2[i]+lx3[i]+b)-b);
            for i in v:
                if i>0:
                    lyoptenida.append(1);
                else:
                    lyoptenida.append(0);
            for i in range(len(lydes)):
                temp.append(lydes[i]-lyoptenida[i]);
                if (temp[i]!=crit):
                    w1=w1+tasa*(temp[i])*lx1[i];
                    w2=w2+tasa*(temp[i])*lx2[i];
                    w3=w3+tasa*(temp[i])*lx3[i];
                    b = b + a *temp[i];
            print("Iteracion:",itera,"Nuevo W1:",w1,"Nuevo W2:",w2,"Nuevo W3:",w3,"Nuevo b:",b);
            itera+=1
            
        
        fig.canvas.draw();


def limpiarGraf():
    ax.cla();
    coordsx1.clear();
    coordsx2.clear();
    coordsx3.clear();
    lx1.clear();
    lx2.clear();
    lydes.clear();
    lyoptenida.clear();
    v.clear();
    temp.clear()
    dataset.clear()
    ax.grid();
    fig.canvas.draw();

fig=Figure(figsize=(5,5));
ax=fig.add_subplot(111,projection='3d');
#ax.set_xlim(-1,1);
#ax.set_ylim(-1,1);

ax.grid()

canvas = FigureCanvasTkAgg(fig, master=window);
canvas.get_tk_widget().grid(row=2,column=0,columnspan=2, rowspan=3);

CFLabel=Label(text="Criterio Finalización:");
CFLabel.grid(row=2,column=2);
cuadroCF=Entry();
cuadroCF.grid(row=2,column=3,padx=padding,pady=padding,columnspan=2);

epLabel=Label(text="Épocas:");
epLabel.grid(row=3,column=2);
cuadroEp=Entry();
cuadroEp.grid(row=3,column=3,padx=padding,pady=padding,columnspan=2);

tazaLabel=Label(text="Tasa:");
tazaLabel.grid(row=4,column=2);
cuadrotaza=Entry();
cuadrotaza.grid(row=4,column=3,padx=padding,pady=padding,columnspan=2);

tazaLabel=Label(text="Tasa:");
tazaLabel.grid(row=4,column=2);
cuadrotaza=Entry();
cuadrotaza.grid(row=4,column=3,padx=padding,pady=padding,columnspan=2);

botonEnvio=Button(text="Iniciar", command=lambda:getEntry());
botonEnvio.grid(row=5,column=0,padx=padding,pady=padding);

botonlim=Button(text="Limpiar", command=lambda:limpiarGraf());
botonlim.grid(row=5,column=1,padx=padding,pady=padding);

BotonAbrir=Button(text="Abrir fichero", command=lambda:abrir());
BotonAbrir.grid(row=1,column=0,padx=padding,pady=padding,columnspan=4);

particionesLabel=Label(text="Particiones:");
particionesLabel.grid(row=0,column=0);
cuadroParticiones=Entry();
cuadroParticiones.grid(row=0,column=1,padx=padding, pady=padding);

pEntrenamientoLabel=Label(text="Porcentaje Entrenamiento:");
pEntrenamientoLabel.grid(row=0,column=2);
cuadroEntrena=Entry();
cuadroEntrena.grid(row=0,column=3,padx=padding,pady=padding);

window.mainloop()