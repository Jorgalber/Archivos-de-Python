# -*- coding: utf-8 -*-
"""
Created on Fri Jan  7 15:15:26 2022

@author: Jorge

For parte 2
"""

def e6():
    num=int(input("escribe un numero: "));
    for i in range(7):
        print(chr(num));
        num=num+1;
#e6();

def e7():
    tope=int(input("dame un numero: "));
    for i in range(tope):
        print("contando ", i);
#e7();

def e8():
    try:
        tope=int(input("dame un numero: "));
        for i in range(tope):
            print("contando ", i);
    except:
        print("Ingresa un numero por favor");
#e8();

def e9():
    for i in [3,4,5]:
        print("el valor de i es: ",i," y su cuadrado es:", i**2);
    print("listo");
    
#e9();

def e10():
    print("Inicio...");
    for i in ["Jorge","Laureano","Glitch","SW"]:
        print("valor de i: ",i);
        
#e10();