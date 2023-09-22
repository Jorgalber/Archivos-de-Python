# -*- coding: utf-8 -*-
"""
Created on Mon Jan 17 14:07:00 2022

@author: Jorge
"""

from tkinter import *;
raiz=Tk();
raiz.title("Prueba");
raiz.resizable();
#raiz.geometry("650x450");
raiz.config(bg="black");
raiz.iconbitmap("icono.ico");

miframe=Frame();
miframe.pack(fill="both",expand=True);
miframe.config(bg="white");
miframe.config(width="650",height="450");
#bordes: miframe.config(bd=5);
#tipo de borde: miframme.config(relief="sunker");
#tipo de cursor: miframe.config(cursor="hand2");

raiz.mainloop();