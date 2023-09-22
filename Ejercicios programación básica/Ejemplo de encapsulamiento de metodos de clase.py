# -*- coding: utf-8 -*-
"""
Created on Sat Jan 22 16:02:35 2022

@author: Jorge
"""

class Coche():
    #constructor
    def __init__(self):
        self.largoChasis=250;
        self.achoChasis=120;
        #variable encapsulada
        self.__ruedas=4;
        self.enMarcha=False;
    
    #metodos
    def arrancar(self,arrancamos):
        self.enMarcha=arrancamos
        if(self.enMarcha):
            check=self.__chequeo();
        
        if (self.enMarcha and check):
            return "El coche esta en marcha";
        elif(self.enMarcha and check==False):
            return"Algo salio mal en el chequeo"
        else:
            return "El coche esta detenido";
            
    def estado(self):
        print("El coche tiene: ",self.__ruedas," ruedas. Un ancho de: ", self.achoChasis," y un largo de: ",self.largoChasis)
    #metodo encapsulado
    def __chequeo(self):
        print("Realizando Chequeo");
        self.gasolina="ok";
        self.aceite="ok";
        self.puertas="cerradas";
        
        if(self.gasolina=="ok" and self.aceite=="ok" and self.puertas=="cerradas"):
            return True
        else:
            return False


miCoche=Coche();
print(miCoche.arrancar(True));
miCoche.estado();

print(".....Nuevo objeto......");

miCoche2=Coche();
print(miCoche2.arrancar(False));
miCoche2.estado();
