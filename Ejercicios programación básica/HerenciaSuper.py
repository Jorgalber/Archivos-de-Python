# -*- coding: utf-8 -*-
"""
Created on Wed Jan 26 15:46:13 2022

@author: Jorge

Ejemplo de instanciacion con super
"""

class Persona():
    def __init__(self, nombre, edad, residencia):
        self.nombre=nombre;
        self.edad=edad;
        self.residencia=residencia;
    
    def Descripcion(self):
        print("Nombre: ",self.nombre,
              "\nEdad: ",self.edad,
              "\nResidencia: ",self.residencia)

class Empleado(Persona):
    def __init__(self,salario,antiguedad,nombreEmp,edadEmp,residEmp):
        super().__init__(nombreEmp, edadEmp, residEmp);
        self.salario=salario;
        self.antiguedad=antiguedad;
    
    def Descripcion(self):
        super().Descripcion();
        print("Salario:",self.salario,
              "\nAntiguedad: ",self.antiguedad)
        
antonio=Empleado(12345,20,"Antonio",55,"Rusia");
antonio.Descripcion();
print(isinstance(antonio, Persona));

Manuel=Persona("Manuel",55,"Rusia");
print(isinstance(Manuel, Empleado));
