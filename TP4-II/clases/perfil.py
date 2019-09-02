# -*- coding: utf-8 -*-

class Perfil:
    """
    Clase Perfil para almacenar información básica de Perfiless de un
    sistema de redes sociales
    """
    alias = ''
    identificador = ''

    def __init__(self, un_id, un_alias):
        """
        método constructor de la clase
        """
        self.alias = un_alias
        self.identificador = un_id

    def __str__(self):
        """
        representación en forma de string del objeto
        """
        return 'identificador del perfil:' + str(self.identificador)
    
    def getalias(self):
        """
        Método que devuelve el alias de la Perfil
        """
        return self.alias
    
    def getId(self):
        """
        Método que devuelve el identificador de la Perfil
        """
        return self.identificador

    
