#!/usr/bin/env python
# -*- coding: utf-8 -*-
class Calculadora(): #Creamos la clase Calculadora
    def __init__(self, operando1, operando2): #Definimos el parametro operando1, operando2 
        self.operando1 = operando1 # Asignamos valor al atributo operando1
        self.operando2 = operando2 # Asignamos valor al atributo operando2
        
      
   #Creacion del metodo sum
    def sum(self):
       for operando in (self.operando1, self.operando2):
        if not isinstance(operando, int) and not isinstance(operando, float):
            raise TypeError
       return self.operando1 + self.operando2