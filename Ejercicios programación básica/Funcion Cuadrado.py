# -*- coding: utf-8 -*-
"""
Created on Wed Jul 13 21:56:16 2022

@author: Jorge
"""

def cuadrado(n):
    if n==0:
        return 0
    else:
        #return 2*n+cuadrado(n-1)-1 
        return 2*n+((n-1)**2)-1
    
x=int (input("Ingresa un numero:"))
print("El cuadrado de ",x,"es",cuadrado(x)) 
