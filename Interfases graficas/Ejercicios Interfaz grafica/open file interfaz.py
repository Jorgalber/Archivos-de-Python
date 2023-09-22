# -*- coding: utf-8 -*-
"""
Created on Thu Jan 20 15:45:07 2022

@author: Jorge
"""
from tkinter import*
from tkinter import filedialog

raiz=Tk();

def abrir():
    fichero=filedialog.askopenfilenames(title="Abrir", initialdir="C:",filetypes=(("Ficheros de Excel","*.xlsx"),
                                                                                  ("ficheros de texto","*.txt"),("Todos los archivos","*.*")));
    print(fichero)
    
Button(raiz, text="Abrir fichero", command=abrir).pack();

raiz.mainloop();