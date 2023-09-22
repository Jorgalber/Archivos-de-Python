# -*- coding: utf-8 -*-
"""
Created on Fri Jan  7 16:14:37 2022

@author: Jorge

Colorama

cuando se usa colorma no se puede llamar al archivo colorama por que enloquese
"""

def e1():
    from colorama import init
    init();
    
def e2():
    from colorama import init, Back, Fore;
    init();
    print(Back.GREEN + Fore.LIGHTYELLOW_EX + "Jorge");

def e3():
    from colorama import init, Back, Fore;
    init();
    print(Back.GREEN + Fore.LIGHTYELLOW_EX + "Jorge");
    print("hola lalala");
    input();

def e4():
    from colorama import init, Back, Fore, Style;
    init();
    print(Style.DIM + "Jorge");
    print(Style.NORMAL + "hola");
    print(Style.BRIGHT + "tu");
    print(Style.NORMAL + "Como", Style.RESET_ALL + Fore.GREEN +"Estas");
    input();

def e5():
    from colorama import init, Fore, Back;
    init(autoreset=True);
    print(Fore.WHITE + Back.BLUE + "HOLA");
    print("Hola");
    input();

def e6():
    from time import sleep;
    from colorama import Cursor, init, Fore;
    init();
    #init(autoreset=True);
    print("Moviendo figura a una posicion...");
    for progress in ["*-----","-*----","--*---","---*--","----*-","-----*"]:
        sleep(1);
        print(Cursor.POS(37,3) + Fore.LIGHTYELLOW_EX + str(progress));
    print(Cursor.POS(37,3) + Fore.LIGHTYELLOW_EX + "Terminado");
    input();
e6();