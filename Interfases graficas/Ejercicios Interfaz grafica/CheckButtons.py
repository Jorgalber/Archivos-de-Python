# -*- coding: utf-8 -*-
"""
Created on Wed Jan 19 14:50:40 2022

@author: Jorge
"""

from tkinter import *;
raiz=Tk();
raiz.title("Check buttons");
raiz.iconbitmap("icono.ico");
marco=Frame(raiz,width=600, height=400);
marco.pack()

playa=IntVar();
montaña=IntVar();
pueblos=IntVar();

def opcViaje():
    opc="";
    if (playa.get()==1):
        opc +=" Playa"
    if (montaña.get()==1):
        opc +=" Montaña"
    if (pueblos.get()==1):
        opc +=" Pueblos"
        
    textoFinal.config(text=opc);

foto=PhotoImage(file="avion.png");
Label(marco,image=foto).grid(row=1,column=1);

Label(marco, text="Elige destino:",width=50).grid(row=2,column=1)
Checkbutton(marco,text="Playa",variable=playa,onvalue=1,offvalue=0,command=opcViaje).grid(row=3,column=1);
Checkbutton(marco,text="Montaña",variable=montaña,onvalue=1,offvalue=0,command=opcViaje).grid(row=4,column=1);
Checkbutton(marco,text="Pueblos",variable=pueblos, onvalue=1,offvalue=0,command=opcViaje).grid(row=5,column=1);

textoFinal=Label(marco);
textoFinal.grid(row=6,column=1);

raiz.mainloop();