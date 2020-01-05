# -*- coding: utf-8 -*-

class Personaje:
    """
    Clase donde se guarda la informacion sobre personajes
    
    Args:
        
    """
    
    def __init__(self):
        self.__nombres= dict()
        self.__pospers = dict()
        self.lennombres = dict()
        self.__numapar = 0
        
    def getPersonaje(self):
        """
        Metodo que devuelve un diccionario con todos los nombres del personaje y sus apariciones
        
        Args:
            
        Return:
            diccionario con los nombres y posiciones del personaje por cada nombre
        """
        return self.__nombres
    
    def getPosicionPers(self):
        """
        Metodo que devuelve un diccionario de todas las posiciones en las que sale el personaje
        por cada capitulo
    
        Args:
            
        Return:
            diccionario de posiciones del personaje por capitulo
        """
        return self.__pospers
    
    def setPosicionPers(self,pospers):
        """
        Metodo para establecer un diccionario de todas las posiciones en las que sale el personaje
        por cada capitulo
    
        Args:
            las posiciones del personaje por capitulo
        """
        self.__pospers = pospers
    
    def getNumApariciones(self):
        """
        Metodo que devuelve el numero de apariciones de un pesonaje y si todos los personajes de este
        tienen las posiciones encontradas
    
        Args:
            
        Return:
            numero de apariciones
            todos los nombes con las posiciones encontradas
        """
        for k in self.__nombres.keys():
            if k not in self.lennombres:
                return self.__numapar,False
        return self.__numapar,True
    
    def sumNumApariciones(self,apar):
        """
        Metodo que añade un numero de apariciones a un pesonaje
    
        Args:
            apar: numero de apariciones a añadir
        """
        self.__numapar += apar
        
    def resNumApariciones(self,apar):
        """
        Metodo que elimina un numero de apariciones a un pesonaje
    
        Args:
            apar: numero de apariciones a eliminar
        """
        self.__numapar -= apar