# -*- coding: utf-8 -*-

from .perfil import Perfil


class Comentario:
    """
    Clase Comentario para almacenar información básica de Comentarios de un
    red social
    """
    owner=''
    identificador=''
    texto=''

    def __init__(self, un_id, un_owner):
        """
        método constructor de la clase
        """
        if isinstance(un_owner, Perfil):
            self.owner=un_owner
            self.identificador = un_id

    def __str__(self):
        """
        representación en forma de string del objeto
        """
        return 'identificador del comentario: ' + str(self.identificador)
    
    def getOwner(self):
        """
        Método que devuelve el Owner de la Comentario
        """
        return self.owner
    
    def getId(self):
        """
        Método que devuelve el identificador de la Comentario
        """
        return self.identificador
    
    def getContenido(self):
        """
        Método que devuelve el texto de la Comentario
        """
        return self.texto

    def setContenido(self, un_contenido):
        """
        Método que agrega o vincula un_contenidos a un Comentario
        """
        self.texto = un_contenido
