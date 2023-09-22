# -*- coding: utf-8 -*-
"""
Created on Mon Jan 17 15:49:58 2022

@author: Jorge
"""

from tkinter import *;
raiz=Tk();
raiz.title("Prueba de label");
raiz.iconbitmap("icono.ico");
marco=Frame(raiz,width=600, height=400);
marco.pack()

milabel=Label(marco,text="Esto es una Prueba");
milabel.place(x=100,y=300);

Label(marco,text="Hola",fg="red",font=("Comic Sans MS",18)).place(x=200);

imagen=PhotoImage(file="Moguri_KHX.png");

Label(marco,image=imagen).place(x=200,y=300);

raiz.mainloop();