# -*- coding: utf-8 -*-

class Pila:
    """
    Pilas: estructura de datos LIFO: last in, first out (ultimo en entrar, primero en salir)
    Se pueden acumular elementos en forma de pila, como uno arriba del otro.
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
        return 'Pila: ' + self.lista.__str__()
    
    def pilaVacia(self):
        """
        Devuelve True si la Pila está vacia. False, caso contrario
        """
        return len(self.lista) == 0

    def apilar(self, un_elemento):
        """
        Pone en el tope de la pila a 'un_elemento'
        """
        self.lista.insert(0,un_elemento)
    
    def tope(self):
        """
        Devuelve el elemento en el tope de la Pila
        """
        if not self.pilaVacia():
            return self.lista[0]
        else:
            None
    
    def desapilar(self):
        """
        Elemina el elemento del tope de la Pila.
        """
        if not self.pilaVacia():
            self.lista.pop(0)
    
    
