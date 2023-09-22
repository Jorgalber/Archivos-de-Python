# -*- coding: utf-8 -*-
"""
Created on Mon Jul 25 16:26:57 2022

@author: Jorge
"""

def sumlen(b):
    a=0;
    while(b>0):
        a+=1;
        b-=1;
    return a,b;

x=int (input("Ingresa un numero: "))
r1,r2=sumlen(x);
print("Ingresaste: ",x," y ahora es ",r2," y el resultado de la suma lenta es ",r1) 
