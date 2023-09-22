# -*- coding: utf-8 -*-
"""
Created on Mon Jan 24 13:53:42 2022

@author: Jorge
"""

class Vehiculos():
    def __init__(self,marca, modelo):
        self.marca=marca;
        self.modelo=modelo;
        self.enMarcha=False;
        self.acelera=False;
        self.frena=False;
    
    def arrancar(self):
        self.enMarcha=True;
    
    def acelerar(self):
        self.acelera=True;
    
    def frena(self):
        self.frena=True;
    
    def estado(self):
        print("Marca: ",self.marca,
              "\nModelo: ",self.modelo,
              "\nEn Marcha: ",self.enMarcha,
              "\nAcelerando: ",self.acelera,
              "\nFrenando: ",self.frena)

class Camioneta(Vehiculos):
    def carga(self,carga):
        self.cargado=carga;
        if(self.cargado):
            return "Esta cargada"
        else:
            return"No esta cargada"

class Moto(Vehiculos):
    hcaballito="";
    
    def caballito(self):
        self.hcaballito="Esta haciendo una acrobacia";
    
    def estado(self):
        print("Marca: ",self.marca,
              "\nModelo: ",self.modelo,
              "\nEn Marcha: ",self.enMarcha,
              "\nAcelerando: ",self.acelera,
              "\nFrenando: ",self.frena,
              "\n",self.hcaballito)

class Velect(Vehiculos):
    def __init__(self,marca,modelo):
        super().__init__(marca,modelo)
        self.autonomia=100;
    def cargaEne(self):
        self.cargando=True;
        
#herencia multiple da preferencia a la primera en ponerse
class BiciElec(Velect,Vehiculos):
    pass
    

miMoto=Moto("Honda","CBR" )
miMoto.caballito();
miMoto.estado();

miCamioneta=Camioneta("Renault", "Kongoo")
miCamioneta.arrancar();
miCamioneta.estado();
print(miCamioneta.carga(True));

miBici=BiciElec("Orbea","q123");
miBici.estado();
