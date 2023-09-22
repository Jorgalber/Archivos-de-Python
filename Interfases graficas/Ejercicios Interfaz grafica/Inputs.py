# -*- coding: utf-8 -*-
"""
Created on Mon Jan 17 16:14:29 2022

@author: Jorge

prueba de labels y inputs ordenandolos mediante grid
"""

from tkinter import *;
raiz=Tk();
raiz.title("Entry");
raiz.iconbitmap("icono.ico");
marco=Frame(raiz,width=600, height=400);
marco.pack()

padding=20;

miNombre=StringVar()

Label(marco,text="Prueba").grid(row=0,column=1,padx=padding,pady=padding);

cuadroNombre=Entry(marco, textvariable=miNombre);
cuadroNombre.grid(row=1,column=1,padx=padding,pady=padding);
cuadroNombre.config(fg="blue", justify="center");

cuadroApellido=Entry(marco);
cuadroApellido.grid(row=2,column=1, padx=padding,pady=padding);

cuadroPass=Entry(marco);
cuadroPass.grid(row=3,column=1, padx=padding,pady=padding);
cuadroPass.config(show="*");

textocomentario=Text(marco,width=20,height=10);
textocomentario.grid(row=4,column=1,padx=padding, pady=padding);

scrollVert=Scrollbar(marco,command=textocomentario.yview);
scrollVert.grid(row=4,column=2, sticky="nsew");

textocomentario.config(yscrollcommand=scrollVert.set);

nombreLabel=Label(marco,text="Nombre:");
nombreLabel.grid(row=1,column=0, padx=padding,pady=padding);

ApeLabel=Label(marco,text="Apellido:");
ApeLabel.grid(row=2,column=0, sticky="e",padx=padding,pady=padding);

PassLabel=Label(marco,text="Password:");
PassLabel.grid(row=3,column=0,padx=padding,pady=padding);

TextLabel=Label(marco,text="Comentarios:");
TextLabel.grid(row=4,column=0,padx=padding,pady=padding);

def codigoBoton():
    miNombre.set("Jorge");
    
    
botonEnvio=Button(raiz,text="Enviar", command=codigoBoton);
botonEnvio.pack();

raiz.mainloop();