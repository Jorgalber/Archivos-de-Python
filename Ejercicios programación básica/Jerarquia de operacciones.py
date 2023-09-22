# -*- coding: utf-8 -*-
"""
Created on Sun Dec 26 19:43:40 2021

@author: Jorge
"""

# Prueba de jerarquia de operaciones

a=80;
b=90;
c=100;

r1=a+b+c;
r2=a*b+c;
r3=a**2-2;
r4=a/b**c/a;

print("R1: ",r1);
print("R2: ",r2);
print("R3: ",r3);
print("R4: ",r4);

r1=a+b+c;
r2=a*b+c;
r3=a**(2-2);
r4=a/b**(c/a);

print("R1: ",r1);
print("R2: ",r2);
print("R3: ",r3);
print("R4: ",r4);