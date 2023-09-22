#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 19 15:59:22 2022

@author: glitch
"""
import tkinter as tk;
from tkinter import filedialog as fd
from tkinter import END

def abrir():
    filetypes=(('Archivo de Texto', '*.txt'),('Todos los archivos','*.*'))
    file=fd.askopenfilename(filetypes=filetypes)
    file=open(file, 'r')
    datos=file.read()
    textA.delete('1.0',END)
    textA.update()
    textA.insert(END,datos)
    file.close()
    
def guardar():
    filetypes=(('Archivo de Texto', '*.txt'),('Todos los archivos','*.*'))
    cadena=textA.get('1.0',END)
    file=fd.asksaveasfile(filetypes=filetypes,mode='w')
    try:
        file.write(cadena)
        file.close()
        botonG.config(text='Guardado')
        botonG.after(3000,lambda:botonG.config(text='Guardar'))
    except:
        print("Error")
    
    
ventana=tk.Tk();
ventana.title("Editor de Texto")

label=tk.Label(text="Editor de Texto");
label.grid(row=0,column=0,pady=10,columnspan=2)
textA=tk.Text(ventana,width=40, height=20)
textA.grid(row=1,column=0, pady=10,padx=20,columnspan=2)
botonA=tk.Button(text="Abrir", command=lambda:abrir())
botonA.grid(row=2,column=0, pady=10,padx=10)
botonG=tk.Button(text="Guardar", command=lambda:guardar())
botonG.grid(row=2,column=1, pady=10,padx=10)

ventana.mainloop();

