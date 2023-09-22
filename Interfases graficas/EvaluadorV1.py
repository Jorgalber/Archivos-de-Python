# -*- coding: utf-8 -*-
"""
Created on Fri Jul 29 15:38:45 2022

@author: Jorge

"""

import tkinter as tk;
from tkinter import Scrollbar;
from tkinter import NONE;
from tkinter import filedialog as fd
from tkinter import END
import pandas as pd

ventana=tk.Tk();
ventana.title("Evaluador")
ventana.iconbitmap("icono.ico")

listaRespC=[]
listaResp=[]
Comp=[]
promedio=0
suma=0
def abrirA():
    global listaRespC
    listaRespC=[]
    files=(('Archivo de Texto (.CSV)', '*.csv'),('Todos los archivos','*.*'))
    file=fd.askopenfilenames(filetypes=files)
    dataset=pd.read_csv(file[0], names=["Respuesta"], header=None)
    x1=dataset.iloc[:,0].values
    for i in x1:
        listaRespC.append(i);
    textA.delete('1.0',END)
    textA.update()
    textA.insert(END,dataset)
    return listaRespC;

def abrirB():
    global listaResp
    listaResp=[]
    files=(('Archivo de Texto (.CSV)', '*.csv'),('Todos los archivos','*.*'))
    file=fd.askopenfilenames(filetypes=files)
    dataset=pd.read_csv(file[0], names=["Respuesta"], header=None)
    x1=dataset.iloc[:,0].values
    for i in x1:
        listaResp.append(i);
    textB.delete('1.0',END)
    textB.update()
    textB.insert(END,dataset)
    return listaResp;

def comparacion(listaA,listaB):
    global promedio,suma
    Comp=[]
    promedio=0
    suma=0
    idx=0
    for i in listaA:
        if i == i in listaB[idx]:
            Comp.append(10);
            idx +=1
        else:
            Comp.append(0);
            idx += 1
    suma=sum(Comp);
    promedio=suma/len(Comp)
    LabelCal.config(text=(promedio))
    return suma,promedio
    

"""
Área de respuestas corrctas 
"""
labelA=tk.Label(ventana,text="Respuestas del Examen")
labelA.grid(row=0,column=1)
textA=tk.Text(ventana,width=20, height=10, wrap=NONE)
textA.grid(row=1,column=1, pady=10,padx=20)

scrollVert=Scrollbar(command=textA.yview);
scrollVert.grid(row=1,column=0, sticky="nsew");
scrollHor=Scrollbar(command=textA.xview,orient='horizontal');
scrollHor.grid(row=2,column=1, sticky="nsew");

textA.config(yscrollcommand=scrollVert.set);
textA.config(xscrollcommand=scrollHor.set);

botonAbrirA=tk.Button(text="Abrir",command=lambda:abrirA())
botonAbrirA.grid(row=3,column=1,pady=10,padx=20);
"""
Área de respuestas a evaluar
"""
labelB=tk.Label(ventana,text="Tus respuestas del Examen")
labelB.grid(row=0,column=3)
textB=tk.Text(ventana,width=20, height=10, wrap=NONE)
textB.grid(row=1,column=3, pady=10,padx=20)

scrollVert=Scrollbar(command=textB.yview);
scrollVert.grid(row=1,column=4, sticky="nsew");
scrollHor=Scrollbar(command=textB.xview,orient='horizontal');
scrollHor.grid(row=2,column=3, sticky="nsew");

textB.config(yscrollcommand=scrollVert.set);
textB.config(xscrollcommand=scrollHor.set);

botonAbrirB=tk.Button(text="Abrir",command=lambda:abrirB())
botonAbrirB.grid(row=3,column=3,pady=10,padx=20);

botonEvaluar=tk.Button(text="Evaluar",command=lambda:comparacion(listaRespC, listaResp))
botonEvaluar.grid(row=4,column=2,pady=10,padx=20);
"""
Área de Resultados
"""
LabelCal1=tk.Label(ventana, text= 'Promedio: ')
LabelCal1.grid(row=5,column=1)

LabelCal=tk.Label(ventana)
LabelCal.grid(row=5,column=2)

ventana.mainloop();