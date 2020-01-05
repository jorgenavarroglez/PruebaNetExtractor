# -*- coding: utf-8 -*-

class TempBD:
    """
    Clase que crea una base de datos temporal para cada sesion de usuario
    
    Args:
        
    """
    __instance = None
    
    def __init__(self):
        if TempBD.__instance is not None:
            raise Exception("An instance already exists!")
        self.__sesiones = dict()
        self.__nextID = 0
        if(TempBD.__instance == None):
            TempBD.__instance = self
            
    @staticmethod
    def getInstance():
        """
        Metodo que devuelve la misma instancia de la clase
        
        Args:
            
        """
        if(TempBD.__instance == None):
            TempBD()
        return TempBD.__instance
    
    def addSesion(self, sesionObject):
        """
        Metodo para anadir un nuevo objeto sesion
        
        Args:
            sesionObject: nuevo objeto sesion
        Return:
            id para acceder al objeto
        """
        self.__nextID += 1
        self.__sesiones[self.__nextID] = sesionObject
        return self.__nextID
    
    def delSesion(self, sesionID):
        """
        Metodo para eliminar un objeto sesion
        
        Args:
            sesionID: id del objeto sesion
        """
        del self.__sesiones[sesionID]
        
    def replaceObject(self, sesionID, sesionObject):
        """
        Metodo para sustituir un objeto sesion por otro
        
        Args:
            sesionID: id de la sesion donde esta el objeto a sustituir
            sesionObject: nuevo objeto sesion
        """
        self.__sesiones[sesionID] = sesionObject
        
    def getObject(self, sesionID):
        """
        Metodo para devuelve un nuevo objeto sesion
        
        Args:
            sesionID: id del objeto a devolver
        """
        return self.__sesiones[sesionID]
    
    def getSesiones(self):
        """
        Metodo para devuelve todas las sesiones
        
        Args:
            diccionario de sesiones
        """
        return self.__sesiones