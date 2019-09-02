# -*- coding: utf-8 -*-

from .perfil import Perfil
from .comentario import Comentario
import random
import datetime

class Post:
    """
    Clase Post para almacenar información básica de Posts de un
    red social
    """
    owner=''
    identificador=''
    texto=''
    comentarios = []
    fecha = ''

    def __init__(self, un_id, un_owner, un_texto):
        """
        método constructor de la clase
        """
        if isinstance(un_owner, Perfil):
            self.owner = un_owner
            self.identificador = un_id
            self.fecha = datetime.date(2018,random.randint(1,12),random.randint(1,28))
            self.texto = un_texto
            self.comentarios = []
        else:
            print('Owner debe ser de la clase Perfil')

    def __str__(self):
        """
        representación en forma de string del objeto
        """
        return 'identificador del post: ' + str(self.identificador)
    
    def getOwner(self):
        """
        Método que devuelve el Owner de la Post
        """
        return self.owner
    
    def getId(self):
        """
        Método que devuelve el identificador de la Post
        """
        return self.identificador
    
    def getFecha(self):
        """
        Método que devuelve la fecha del Post
        """
        return self.fecha
    
    def getContenido(self):
        """
        Método que devuelve el contenido de la Post
        """
        return self.texto
    
    def getComentarios(self):
        """
        Devuelve un conjunto (SET) con todos los comentarios del post
        """
        return self.comentarios

    def setContenido(self, un_contenido):
        """
        Método que agrega o vincula un_contenidos a un Post
        """
        self.texto = un_contenido
    
    def addComentario(self, un_comentario):
        """
        Metodo que agregar un objeto comentario en el post
        """
        if isinstance(un_comentario, Comentario):
            self.comentarios.append(un_comentario)
        else:
            print('comentario debe ser de la clase Comentario')
            return None
    
