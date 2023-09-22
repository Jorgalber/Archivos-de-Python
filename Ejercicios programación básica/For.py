# -*- coding: utf-8 -*-
"""
Created on Sun Jan  2 15:51:33 2022

@author: Jorge

Uso de for
"""

def e1():
    print("----- Ejemplo 1 -----");
    #nombre=["","",""];
    #nombre=[None]*3
    cont=int(input("Cuantos nombres a capturar: "));
    nombre=[None]*cont;
    num=0;
    while num< cont:
        nombre[num]=str(input("Escribe el nombre: "));
        num=num+1
    print(nombre);
#e1();

def e2():
    print("----- Ejemplo 2 -----");
    cont=int(input("Numero de nombres a capturar: "));
    nombre=[None]*cont;
    for num in range(cont):
        print(num);
        nombre[num]=str(input("Escribe el nombre: "));
    print(nombre);
    
#e2();

def e3():
    print("----- Ejemplo 2 -----");
    cont=int(input("Numero de nombres a capturar: "));
    nombre=[None]*cont;
    for num in range(cont):
        print(num);
        minusculas=str(input("dame el nombre: "));
        nombre[num]=str.lower(minusculas);
    print(nombre);
    
    buscar=str(input("Nombre a buscar: "));
    minusculas=str.lower(buscar);
    if minusculas in nombre:
        print("encontrado");
    else:
        print("no encontrado");
#e3();

def e4():
    cont=int(input("Cuantos numeros a capturar: "));
    lista=[None]*cont;
    for num in range(cont):
        lista[num]= int(input("Ingresa algo: "));
    print(lista);
    
#e4();

def e5():
    try:
        cont=int(input("Cuantos numeros a capturar: "));
        lista=[None]*cont;
        for num in range(cont):
            lista[num]= int(input("Ingresa algo: "));
        print(lista);
    except:
        print("Por favor escribe en numeros");
        e5();
    
e5();