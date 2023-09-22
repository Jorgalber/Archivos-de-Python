# -*- coding: utf-8 -*-
"""
Created on Wed Jan 19 14:31:10 2022

@author: Jorge

radio boton
"""

from tkinter import *;
raiz=Tk();
raiz.title("Radio buttons");
raiz.iconbitmap("icono.ico");
marco=Frame(raiz,width=600, height=400);
marco.pack()

varOpc=IntVar();

def imprimir():
    #print(varOpc.get());
    if varOpc.get()==1:
        etiqueta.config(text="Has elegido Masculino");
    else:
        etiqueta.config(text="Has elegido Femenino");

Label(marco,text="Genero").grid(row=1,column=1)

Radiobutton(marco, text="Masculino",variable=varOpc, value=1, command=imprimir).grid(row=2,column=1);
Radiobutton(marco, text="Femenino",variable=varOpc, value=2, command=imprimir).grid(row=3,column=1);

etiqueta=Label(marco);
etiqueta.grid(row=4,column=1);

raiz.mainloop();