# -*- coding: utf-8 -*-
"""
Created on Fri Jan 14 16:25:14 2022

@author: Jorge

diccionarios
"""

def e1():
    horario={};
    horario["lunes"]=[700, 1300];
    buscar= str(input("Dame el dia a buscar: "));
    if buscar in horario:
        print("Encontrado");
        print(horario[buscar]);
def e2():
    horario={};
    dias=0;
    while dias < 3:
        dia=str(input("Dame el dia de a semana: "));
        inicio=str(input("dame la hora de inicio: "));
        final=str(input("dame la hora final: "));
        horario[dia]=[inicio,final];
        dias=dias+1;
    print(horario);

def e3():
    horario={};
    dias=0;
    while dias < 3:
        dia=str(input("Dame el dia de a semana: "));
        inicio=str(input("dame la hora de inicio: "));
        final=str(input("dame la hora final: "));
        horario[dia]=[inicio,final];
        dias=dias+1;
    for dias in horario:
        print(dias," : ",horario[dias]);

def imprime():
    e2();

imprime();