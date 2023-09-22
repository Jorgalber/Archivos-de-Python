# -*- coding: utf-8 -*-
"""
Created on Tue Jul 12 17:30:51 2022

@author: Jorge
"""

def factorial(n):
    if n<0:
        print("Negativo")
    elif(n==1 or n==0):
        return 1
    else:
        fact=1
        while(n>1):
            fact*=n
            n-=1
        return fact

x=int (input("Ingresa un numero:"))
print("El factorial de ",x,"es", factorial(x)) 