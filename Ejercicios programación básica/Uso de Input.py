# -*- coding: utf-8 -*-
"""
Created on Sun Dec 26 20:49:03 2021

@author: Jorge

Prueba de input
a darle atomos 
"""

def suma():
    a=float(input("Dame un primer Numero: "));
    b=float(input("Dame un segundo Numero: "));
    r=a+b;
    return r;

#print("Suma: ",suma());

def name():
    nombre=str(input("Escribe tu nombre: "));
    apellido=str(input("escribe tu apellido: "));
    datos=nombre+" "+apellido;
    return datos;

#print("¡Hola ",name(),"!");

def areaCirculo():
    pi=3.141516;
    radio=float(input("Escribe el radio de tu circulo: "));
    area=pi*(radio**2);
    return area;
print("El area es: ",areaCirculo())