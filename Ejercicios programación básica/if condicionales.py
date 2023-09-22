# -*- coding: utf-8 -*-
"""
Created on Sun Jan  2 14:28:53 2022

@author: Jorge

Uso de la sentencia If
"""

def ejemplo():
    salario=float(input("Ingresa el salario: "));
    print("Usted ingreso: $",salario);
    print("Usted Gana %d ..." %salario);
    print("usted ingreso %f ..." %salario);
    print("usted ingreso %.2f ..." %salario);
    print("usted ingreso %.10f ..." %salario);
    
#ejemplo();

def ejemplo2():
    numero=int(input("Escribe un numero: "));
    print("Tu numero es: %x en hexadecimal" %numero);
    print("en octal: %o" %numero);
    print("en decimal: %d" %numero);

#ejemplo2();

def ejercicio3():
    numero=int(input("Escribe un numero: "));
    opc=0;
    escoge=int(input("Escoge una opcion del 1-3: "));
    opc=escoge;
    if opc==1:
        print("Tu numero es: %x en hexadecimal" %numero);
    elif opc==2:
        print("Tu numero es: %o en octal" %numero);
    elif opc==3:
        print("Tu numero es: %d en decimal" %numero);
    else:
        print("opcion no valida");

#ejercicio3();

def ejemplo4():
    dinero=float(input("Escribe tu capital a invertir: "));
    interes=float(input("Escribe el valor de interes: "));
    if interes>=15:
        print("Buena eleccion de banco");
        gana=dinero*interes/100;
        print("Usted Gano %f mas" %gana);
    else:
        print("cambia de banco")
        
ejemplo4();