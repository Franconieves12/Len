# -*- coding: utf-8 -*-

import datetime

class Persona:
    """
    Clase Persona para almacenar información básica de personas
    """
    nombre=''
    apellido=''
    fecha_nacimiento=''
    dni=''

    def __init__(self, un_nombre, un_apellido, una_fecha, un_dni):
        """
        método constructor de la clase
        """
        if isinstance(una_fecha, datetime.datetime):
            self.nombre=un_nombre
            self.apellido=un_apellido
            self.fecha_nacimiento=una_fecha
            self.dni=un_dni
        else:
            print('una_fecha debe ser del tipo datetime')
        

    def __str__(self):
        """
        representación en forma de string del objeto
        """
        return str(self.nombre) + ', ' + self.apellido
    
    def getNombre(self):
        """
        Método que devuelve el nombre de la persona
        """
        return self.nombre
    
    def getApellido(self):
        """
        Método que devuelve el Apellido de la persona
        """
        return self.apellido

    def getDNI(self):
        """
        Método que devuelve el dni de la persona
        """
        return self.dni
    
    def getFechaNacimiento(self):
        """
        Método que devuelve el fecha_nacimiento de la persona
        """
        return self.fecha_nacimiento
    
