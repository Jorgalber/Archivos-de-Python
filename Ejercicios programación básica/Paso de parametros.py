# -*- coding: utf-8 -*-
"""
Created on Thu Jan 13 16:47:02 2022

@author: Jorge

paso de parametros
"""

def suma(a,b):
    return a+b;
def resta(a,b):
    return a-b;
def div(a,b):
    return a/b;
def multi(a,b):
    return a*b;

def e1():
    a=float(input("Escribe un valor: "));
    b=float(input("Escribe otro valor: "));
    print("suma: ", suma(a,b));
    print("resta: ", resta(a,b));
    print("division: ", div(a,b));
    print("Multi: ", multi(a,b));
    
#e1();

def nombre():
    nom=str(input("Escribe tu nombre: "));
    return nom;
def apellido():
    ape=str(input("Escribe tu apellido: "));
    return ape;
def e2():
    concatenar=nombre()+" "+apellido();
    print(concatenar);
#e2(); 
#e2 es con paso de funcion

def concatena(nombre,apellido):
    concat=nombre+" "+apellido;
    return concat;
def e3():
    nom=str(input("Escribe tu nombre: "));
    ape=str(input("Escribe tu apellido: "));
    print(concatena(nom, ape));

#e3 paso de paramapetros
#e3();

def cal_iva(precio,iva):
    nuevoPrecio=precio+(precio*iva/100);
    return nuevoPrecio;
def e4():
    precio=float(input("Escribe el precio: "));
    iva=float(input("Escribe el iva: "));
    print("El valor nuevo: ",cal_iva(precio, iva));

#e4();

def e5():
    lista=[100,16];
    print("precio: con iva: ",cal_iva(*lista))
    
e5();
