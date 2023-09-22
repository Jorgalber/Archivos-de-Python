# -*- coding: utf-8 -*-
"""
Created on Sat Jan 15 16:08:37 2022

@author: Jorge

prueba de Programación Orientada a Objetos
"""
#ejemplo de uso de una clase
class gato:
    especie="mamifero"
    def __init__(self, nombre, edad):
        self.nombre=nombre;
        self.edad=edad;
        self.alimento=[];
    
    def etapaDeVida(self):
        if self.edad>1:
            print(self.nombre," es adulto");
        else:
            print(self.nombre," es cachorro");
    
    def esAlimentoFavorito(self,alimento):
        if alimento in self.alimento:
            print("Le gusta");
            return alimento 
        else:
            print("no le gusta");
        
#ejemplo de herencia entre clases 
class empleado:
    def __init__(self,nombre, edad, sueldo):
        self.nombre=nombre;
        self.edad=edad;
        self.sueldoBase=sueldo;
    
    def calcularSueldoTotal(self, descuentos, bonos):
        return self.sueldoBase-descuentos+bonos;
    
class AgenteVentas(empleado): #si la clase hereda pero tiene mas atributos se hace un init nuevo que os incluya 
    def __init__(self,nombre, edad, sueldo, mostrador):
        self.numMostrador=mostrador;
        super().__init__(nombre, edad, sueldo);# y se envian al padre de esta forma 
        
class tripulante(empleado):
    def renovarLicencia(self):
        if self.edad<45:
            print("renueva en 1 año");
        else:
            print("renueva cada 6 meses");

#ocultamineto
class carrera:
    def __init__(self, nombre):
        self.nombre=nombre;
        self.__materias={};
        
    def agregarMateria(self, materia, codigo):
        self.materias[codigo]=materia;
        
class Materia:
    def __init__(self, nombre, profesor, fecha):
        self.nombre=nombre;
        self.profesor=profesor;
        self.fechaInicioDictado=fecha;
        
    @property
    def fechaInicioDictado(self):
        #El guion bajo antes del self indica qu es un atributo privado
        #print("prueba")
        return self._fechaInicioDictado;
    
    @fechaInicioDictado.setter
    def fechaInicioDictado(self, fecha):
        if fecha<2006:
            self._fechaInicioDictado=2006;
        else:
            self._fechaInicioDictado=fecha;
            
class asalariado:
    def __init__(self,nombre, sueldo):
        self.nombre=nombre;
        self.sueldoBase=sueldo;
    
    def calcularSueldo(self, descuentos):
        return self.sueldoBase-descuentos;

class gerente(asalariado):
    def calcularSueldo(self, descuentos, bonos):
        return self.sueldoBase-descuentos+bonos;
