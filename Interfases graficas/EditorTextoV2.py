# -*- coding: utf-8 -*-
"""
Created on Thu Jun 30 19:15:21 2022

@author: Jorge
"""

import tkinter as tk;
from tkinter import Menu;
from tkinter import Scrollbar;
from tkinter import NONE;
from tkinter import messagebox
from tkinter import filedialog as fd
from tkinter import END
ventana=tk.Tk();
ventana.title("Editor de Texto")
#ventana.iconbitmap("icono.ico")

def infoAdicional():
    messagebox.showinfo("Pocesador de texto", "Version 2 \nJunio de 2022");

def avisoLicencia():
    messagebox.showwarning("Licencia","Tipo de licencia: GNU");

def AvisoSalir():
    valor=messagebox.askokcancel("Salir","¿Deseas salir?");
    if valor==True:
        ventana.destroy();

def nuevo():
    valor=messagebox.askokcancel("Nuevo","¿Deseas crear un nuevo archivo?");
    if valor==True:
        textA.delete('1.0',END)
        textA.update()

def abrir():
    files=(('Archivo de Texto (.txt)', '*.txt'),('Todos los archivos','*.*'))
    file=fd.askopenfilename(filetypes=files)
    file=open(file, 'r')
    datos=file.read()
    textA.delete('1.0',END)
    textA.update()
    textA.insert(END,datos)
    file.close()
    
def guardar():
    files=(('Archivo de Texto (.txt)', '*.txt'),('Todos los archivos','*.*'))
    cadena=textA.get('1.0',END)
    file=fd.asksaveasfile(filetypes=files, mode='w', defaultextension = files)
    try:
        file.write(cadena)
        file.close()
    except:
        print("Error")

def copy():
    global data 
    if textA.selection_get():
        data=textA.selection_get() 

def cut():
    global data 
    if textA.selection_get():
        data=textA.selection_get() 
        textA.delete('sel.first','sel.last') 

def paste():
    global data
    textA.insert(tk.END,data) 
    
barraMenu=Menu(ventana);
ventana.config(menu=barraMenu, width=300, height=300);

archivoMenu=Menu(barraMenu,tearoff=0);
archivoMenu.add_command(label="Nuevo",command=lambda:nuevo());
archivoMenu.add_command(label="Abrir",command=lambda:abrir());
archivoMenu.add_command(label="Guardar",command=lambda:guardar());
archivoMenu.add_separator();
archivoMenu.add_command(label="Salir",command=AvisoSalir);

archivoEdicion=Menu(barraMenu,tearoff=0);
archivoEdicion.add_command(label="Copiar",command=lambda:copy());
archivoEdicion.add_command(label="Cortar",command=lambda:cut());
archivoEdicion.add_command(label="Pegar",command=lambda:paste());

archivoHerramientas=Menu(barraMenu,tearoff=0);
archivoAyuda=Menu(barraMenu,tearoff=0);
archivoAyuda.add_command(label="Licencia",command=avisoLicencia);
archivoAyuda.add_command(label="Acerca de ...", command=infoAdicional);

barraMenu.add_cascade(label="Archivo",menu=archivoMenu);
barraMenu.add_cascade(label="Edición",menu=archivoEdicion);
barraMenu.add_cascade(label="Ayuda",menu=archivoAyuda);

textA=tk.Text(ventana,width=40, height=20, wrap=NONE)
textA.grid(row=0,column=0, pady=10,padx=20)

scrollVert=Scrollbar(command=textA.yview);
scrollVert.grid(row=0,column=1, sticky="nsew");
scrollHor=Scrollbar(command=textA.xview,orient='horizontal');
scrollHor.grid(row=1,column=0, sticky="nsew");

textA.config(yscrollcommand=scrollVert.set);
textA.config(xscrollcommand=scrollHor.set);

ventana.mainloop();