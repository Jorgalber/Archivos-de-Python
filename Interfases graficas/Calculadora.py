# -*- coding: utf-8 -*-
"""
Created on Tue Jan 18 15:20:26 2022

@author: Jorge

Prueba de calculadora con interfaz
"""

from tkinter import *;
raiz=Tk();
raiz.title("Calculadora");
raiz.iconbitmap("icono.ico");
marco=Frame(raiz,width=600, height=400);
marco.pack()

pad=10;

operacion="";
resultado=0;

#-------Pantalla-------#

numPantalla=StringVar();
pantalla=Entry(marco, textvariable=numPantalla);
pantalla.grid(row=1, column=1, padx=pad,pady=pad,columnspan=4);
pantalla.config(background="black",fg="green", justify="right");

#-------Pulsar-------#

def numPulsado(num):
    global operacion
    if operacion !="":
        numPantalla.set(num);
        operacion="";
    else:
        numPantalla.set(numPantalla.get() + num);

#-------Suma-------#  

def suma(num):
    global operacion
    global resultado
    resultado+=float(num);
    operacion="suma";
    numPantalla.set(resultado);
    
#-------Resultado-------# 

def elresultado():
    global resultado
    numPantalla.set(resultado+float(numPantalla.get()));
    resultado=0;

#-------Fila 1-------#

boton7=Button(marco,text="7", width=3, command=lambda:numPulsado("7"));
boton7.grid(row=2,column=1);
boton8=Button(marco,text="8", width=3, command=lambda:numPulsado("8"));
boton8.grid(row=2,column=2);
boton9=Button(marco,text="9", width=3, command=lambda:numPulsado("9"));
boton9.grid(row=2,column=3);
botonDiv=Button(marco,text="/", width=3);
botonDiv.grid(row=2,column=4);

#-------Fila 2-------#

boton4=Button(marco,text="4", width=3, command=lambda:numPulsado("4"));
boton4.grid(row=3,column=1);
boton5=Button(marco,text="5", width=3, command=lambda:numPulsado("5"));
boton5.grid(row=3,column=2);
boton6=Button(marco,text="6", width=3, command=lambda:numPulsado("6"));
boton6.grid(row=3,column=3);
botonMult=Button(marco,text="X", width=3);
botonMult.grid(row=3,column=4);

#-------Fila 3-------#

boton1=Button(marco,text="1", width=3, command=lambda:numPulsado("1"));
boton1.grid(row=4,column=1);
boton2=Button(marco,text="2", width=3, command=lambda:numPulsado("2"));
boton2.grid(row=4,column=2);
boton3=Button(marco,text="3", width=3, command=lambda:numPulsado("3"));
boton3.grid(row=4,column=3);
botonRest=Button(marco,text="-", width=3);
botonRest.grid(row=4,column=4);

#-------Fila 4-------#

botonComa=Button(marco,text=",", width=3, command=lambda:numPulsado(","));
botonComa.grid(row=5,column=1);
boton0=Button(marco,text="0", width=3, command=lambda:numPulsado("0"));
boton0.grid(row=5,column=2);
botonSuma=Button(marco,text="+", width=3, command=lambda:suma(numPantalla.get()));
botonSuma.grid(row=5,column=3);
botonIgual=Button(marco,text="=", width=3,command=lambda:elresultado());
botonIgual.grid(row=5,column=4);

#-------Fila 4-------#

raiz.mainloop();