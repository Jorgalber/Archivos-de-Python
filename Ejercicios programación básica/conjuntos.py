# -*- coding: utf-8 -*-
"""
Created on Thu Jan 13 17:18:07 2022

@author: Jorge

conjuntos
"""

def e1():
    lista=[5,10,10,15,5];
    conjunto=set(lista);
    print(conjunto);

#e1();

def e2():
    tupla=(5,10,10,15,5);
    conjunto=set(tupla);
    print(conjunto);
#e2();

def e3():
    cont=int(input("Cuantos nombres a capturar: "));
    nombre=[None]*cont;
    num=0;
    while num < cont:
        nombre[num]=str(input("Dame un nombre: "));
        num=num+1;
    print("Lista original: ",nombre);
    print("Lista sin repetidos: ",set(nombre));
    print("Sin repetir: ",len(set(nombre)));
    
#e3();

def e4():
    cont=int(input("Cuantos nombres a capturar: "));
    conjunto={""};
    num=0;
    while num < cont:
        nombre=str(input("Dame un nombre: "));
        conjunto.add(nombre);
        num=num+1;
    print(conjunto);
    print("Lista sin repetidos: ",len(set(nombre)));
    num=0;
    buscar=str(input("Nombre a buscar: "));
    if buscar in conjunto:
        print("encontrado... borrando");
        conjunto.remove(buscar);
    else:
        print("No encontrado")
    print(conjunto);
    
#e4();

def e5():
    nombre={"CARLOS","LUIS"};
    apellido={"ALVARES","CARLOS"}
    print("la union -> ",nombre | apellido);
    print("la interseccion -> ",nombre & apellido);
    print("la diferencia -> ",nombre - apellido);
    print("Diferenciasimetrica -> ",nombre ^ apellido);
    
e5();