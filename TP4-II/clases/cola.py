# -*- coding: utf-8 -*-

class Cola:
    """
    Cola: estructura de datos FIFO: first in, first out (primero en entrar, 
    primero en salir)
    """
    lista = []

    def __init__(self):
        """
        metodo constructor de la clase
        """
        self.lista = []

    def __str__(self):
        """
        representación en forma de string del objeto
        """
        return 'Cola: ' + self.lista.__str__()
    
    def colaVacia(self):
        """
        Devuelve True si la Cola está vacia. False, caso contrario
        """
        return len(self.lista) == 0

    def encolar(self, un_elemento):
        """
        Pone en fila de la cola a 'un_elemento'
        """
        self.lista.insert(len(self.lista),un_elemento)
    
    def siguiente(self):
        """
        Devuelve el elemento siguiente en la Cola
        """
        if not self.colaVacia():
            return self.lista[0]
        else:
            None
    
    def desencolar(self):
        """
        Elemina el elemento siguiente de la Cola.
        """
        if not self.colaVacia():
            self.lista.pop(0)
    
    
