# -*- coding: utf-8 -*-
"""
Created on Wed Jan 19 15:23:42 2022

@author: Jorge
"""
from tkinter import*;
from tkinter import messagebox
raiz=Tk();

def infoAdicional():
    messagebox.showinfo("Pocesador de Jorge", "Version de 2022");

def avisoLicencia():
    messagebox.showwarning("Licencia","Es GNU");

def AvisoSalir():
    #valor=messagebox.askquestion("Salir","¿Deseas salir?");
    valor=messagebox.askokcancel("Salir","¿Deseas salir?");
    if valor==True:
        raiz.destroy();

def cerrarDoc():
    valor=messagebox.askretrycancel("Reintentar","¿Deseas reintentar?");
    if valor==False:
        raiz.destroy();

barraMenu=Menu(raiz);
raiz.config(menu=barraMenu, width=300, height=300);

archivoMenu=Menu(barraMenu,tearoff=0);
archivoMenu.add_command(label="Nuevo");
archivoMenu.add_command(label="Guardar");
archivoMenu.add_command(label="Guardar como...");
archivoMenu.add_command(label="Cerrar",command=cerrarDoc);
archivoMenu.add_separator();
archivoMenu.add_command(label="Salir",command=AvisoSalir);

archivoEdicion=Menu(barraMenu,tearoff=0);
archivoEdicion.add_command(label="Copiar");
archivoEdicion.add_command(label="Cortar");
archivoEdicion.add_command(label="Pegar");

archivoHerramientas=Menu(barraMenu,tearoff=0);
archivoAyuda=Menu(barraMenu,tearoff=0);
archivoAyuda.add_command(label="Licencia",command=avisoLicencia);
archivoAyuda.add_command(label="Acerca de ...", command=infoAdicional);

barraMenu.add_cascade(label="Archivo",menu=archivoMenu);
barraMenu.add_cascade(label="Edición",menu=archivoEdicion);
barraMenu.add_cascade(label="Herramientas",menu=archivoHerramientas);
barraMenu.add_cascade(label="Ayuda",menu=archivoAyuda);



raiz.mainloop();