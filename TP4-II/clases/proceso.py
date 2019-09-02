# -*- coding: utf-8 -*-

from clases.usuario import Usuario
import datetime

class Proceso:
    """
    Procesos de sistemas operativos. Todo proeso de un sistema operativo
    está representado básicamente por un PID y un nombre de proceso
    """
    pid = 0
    nombre = ''
    owner = ''
    start_time = ''

    def __init__(self, un_pid, un_datetime, un_nombre, un_owner):
        """
        método constructor de la clase
        """
        if isinstance(un_owner, Usuario): 
            if isinstance(un_datetime, datetime.datetime):
                self.pid = un_pid
                self.nombre = un_nombre
                self.owner = un_owner
                self.start_time = un_datetime
            else:
                print('un_datetime debe ser de la clase datetime')
        else:
            print('Owner debe ser de la clase Usuario')

    def __str__(self):
        """
        representación en forma de string del objeto
        """
        return 'PID: ' + str(self.pid) + ' -- ' + str(self.owner) + \
            ' -- ' + self.nombre
    
    def getPID(self):
        """
        Retorna el PID del proceso
        """
        return self.pid
    
    def getStartTime(self):
        """
        Retorna el datetime del proceso, la fecha y hora de inicio
        """
        return self.start_time
    
    def getNombre(self):
        """
        Retorna el nombre del proceso
        """
        return self.nombre

    def getOwner(self):
        """
        Retorna el usuario que ejecuta el proceso
        """
        return self.owner
