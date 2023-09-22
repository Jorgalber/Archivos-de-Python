# -*- coding: utf-8 -*-
"""
Created on Fri Jan  7 15:32:53 2022

@author: Jorge

For parte 3
"""

def e11():
    mensaje=str(input("Escribe: "));
    print(mensaje);
    mensaje=str.split(mensaje);
    for i in mensaje:
        print("separado: ",i);
    print("lista: ",mensaje);

#e11();

def e12():
    cuenta=0;
    for i in range(5, 10):
        cuenta=cuenta+1;
        print("cuenta: ", cuenta);
#e12();

def e13():
    numero=str(input("Escribe numeros separados por espacio: "));
    print(numero);
    suma=0;
    lista=str.split(numero);
    print(lista);
    lista=[int(i) for i in lista];
    print(lista);
    for i in (lista): 
        suma=suma+i;
    print("la suma de la lista: ",lista, " es ", suma);

#e13();

def e14():
    print("Bibliotecas");
    import time;
    frase=str(input("Escribe algo: "));
    for letra in str(frase):
        print(letra, end="");
        time.sleep(1);
e14();