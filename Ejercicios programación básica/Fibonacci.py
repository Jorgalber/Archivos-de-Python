# -*- coding: utf-8 -*-
"""
Created on Mon Jul 18 16:23:53 2022

@author: Jorge
"""

def fibo(n):
    if (n<=1):
        return 1;
    else:
        return fibo(n-1)+fibo(n-1)

x=int (input("Ingresa un numero:"))
print("El dibonachi de  ",x,"es",fibo(x)) 
