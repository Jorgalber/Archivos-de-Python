# -*- coding: utf-8 -*-
"""
Created on Sun Dec 26 20:01:09 2021

@author: Jorge
"""

# Prueba de un funcion 

a=25.5;
b=90.48;
c=3.1315;

r1=0;
r2="hola";
r3=r1;

#print("R1: ", r1);
#print("R2: ", r2);
#print("R3: ", r3);

#funcion vacia
def blablabla():
    pass;
    
def suma():
    r1=a+b+c;
    print("Suma: ",r1);
    
def resta():
    r5=c-10;
    return r5;

def multiplicacion():
    r6=a*c;
    print("Multiplicación", r6);
    
def divicion():
    r7=c/a;
    return r7;
    
suma();
print("Resta: ",resta());
multiplicacion();
print("División: ",divicion());
