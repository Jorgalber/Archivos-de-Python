# -*- coding: utf-8 -*-
"""
Created on Fri Jan 14 17:12:57 2022

@author: Jorge

manejo de archivos
"""

def e0():
    #archivo=open("datos.txt");
    #archivo=open("datos.txt","r");#r w
    archivo=open("datos.txt",mode="r", encoding="utf-8");
    leer1=archivo.read();
    print(leer1);
    input();
    archivo.close();

def e1():
    archivo=open("datos.txt",mode="r", encoding="utf-8");
    while (True):
        leer=archivo.read(1);
        if not leer:
            break;
        print(leer);
    archivo.close();

def e2():
    archivo=open("datos.txt",mode="r", encoding="utf-8");
    leer=archivo.readlines();
    contador=0;
    for linea in leer:
        contador=contador+1;
        print(contador,linea);
    archivo.close();

def e3():
    nombre=str(input("Nombre del archivo: "));
    archivo=open(nombre,mode="w",encoding="utf-8");
    archivo.close();
    
def e4():
    dias={"lunes","martes","miercoles","miercoles"};
    nombre=str(input("Nombre del archivo: "));
    archivo=open(nombre,mode="a",encoding="utf-8");
    archivo.writelines(dias);
    archivo.close()

def imprime():
    e4();

imprime();