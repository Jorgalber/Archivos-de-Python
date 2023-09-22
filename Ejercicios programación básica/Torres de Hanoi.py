# -*- coding: utf-8 -*-
"""
Created on Tue Jul 12 16:57:31 2022

@author: Jorge
"""

def hanoi(discos,torreOri=1,torreAux=2,torreDes=3):
    if discos==1:
        print("Pasando de Torre: ",torreOri," a Torre",torreDes)
    else:
        hanoi(discos-1,torreOri,torreDes,torreAux)
        print("Pasando de Torre: ",torreOri," a Torre",torreDes)
        hanoi(discos-1,torreAux,torreOri,torreDes)
    return
        

x=int (input("Ingresa un numero:"))
hanoi(x)