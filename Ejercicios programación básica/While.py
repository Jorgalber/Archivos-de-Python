# -*- coding: utf-8 -*-
"""
Created on Sun Jan  2 15:07:38 2022

@author: Jorge

ejemplo de trabajo con la sentencia while
"""

def e1():
    print("----- Ejemplo 1 -----");
    num=0;
    print("Numero: ", num+1);
    print("Numero: ", num+2);
    print("Numero: ", num+3);
    print("Numero: ", num+4);

def e2():
    print("----- Ejemplo 2 -----");
    a=1;
    while(a<=4):
        print("Numero: ",a);
        a=a+1;

def e3():
    print("----- Ejemplo 3 -----");
    a=0;
    while(a<=10):
        print("Numero: ",a)
        a=a+2;

def e4():
    print("----- Ejemplo 4 -----");
    a=1;
    while(a<=10):
        print("Numero: ",a)
        a=a+2;
        
def e5():
    print("----- Ejemplo 5 -----");
    edad=int(input("Ingresa tu edad: "));
    while(edad>0)&(edad<18):
        edad=int(input("Ingresa tu edad valida para la app: "));
    print("Acepta las condiciones")

def e6():
    print("----- Ejemplo 6 -----");
    n=0;
    nombre=str(input("Ingresa tu nombre: "));
    letra=str(input("Escoge una letra de tu nombre: "));
    while letra != nombre[n]:
        print("Posicion: ",n, nombre[n]);
        n=n+1;
    print("Encontrada en la posicion: ",n);


#e1();
#e2();
#e3();
#e4();
#e5();
e6();