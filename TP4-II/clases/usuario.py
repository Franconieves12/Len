# -*- coding: utf-8 -*-

class Usuario:
    """
    Clase Usuario para almacenar información básica de usuarios de un
    sistema informatico
    """
    nombre = ''
    identificador = ''

    def __init__(self, un_id, un_nombre):
        """
        método constructor de la clase
        """
        self.nombre = un_nombre
        self.identificador = un_id

    def __str__(self):
        """
        representación en forma de string del objeto
        """
        return str(self.identificador) + ' - ' + self.nombre
    
    def getNombre(self):
        """
        Método que devuelve el nombre de la usuario
        """
        return self.nombre
    
    def getId(self):
        """
        Método que devuelve el identificador de la usuario
        """
        return self.identificador

    
