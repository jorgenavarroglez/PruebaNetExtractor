# -*- coding: utf-8 -*-
import ply.lex as lex

class CreaDict:
    """
    Clase que crea un diccionario de manera automática
    
    Args:
        modusuario: instancia de la clase modelo
    """
    
    def __init__(self, modusuario):
        self.lexer = lex.lex(module=self)
        self.aux = dict()
        self.mod = modusuario
      
    #Tokens del lexer
    tokens = ("PERSONAJE", "ESPACIOS", "PUNTO", "CARACTER", "OTRO")
    #Estados del lexer
    states = (('punto','exclusive'),)
    
    
    def t_PERSONAJE(self,t): 
        r"[A-Z\300-\335][a-z\340-\377]+((\s|\-)?[A-Z\300-\335]([a-z\340-\377]+|\.))*"
        
        """
        Metodo que detecta los personajes
        
        Args:
            t: token
        Return:
            token coincidencia
        """
        return t

    def t_ESPACIOS(self,t):
        r"[\s]"
        
        """
        Metodo que detecta los espacios
        
        Args:
            t: token
        """

    def t_PUNTO(self,t):
        r"(\.+)|[\(\)\[\]<>\'\":;¿\?¡!=\-_\253\273—]"
        
        """
        Metodo que detecta los signos de puntuacion y cambia de estado
        
        Args:
            t: token
        """
        t.lexer.begin('punto')
        
    def t_CARACTER(self,t):
        r"."
        
        """
        Metodo que detecta los cualquier caracter
        
        Args:
            t: token
        """

    def t_punto_OTRO(self,t):
        r"[^\s\.\(\)\[\]<>\'\":;¿\?¡!=\-_\253\273—]+"
        
        """
        Metodo que detecta los no signos de puntuacion y vuelve al estado inicial
        
        Args:
            t: token
        """
        t.lexer.begin('INITIAL')
        
    def t_punto_ESPACIOS(self,t):
        r"[\s\.\(\)\[\]<>\'\":;¿\?¡!=\-_\253\273—]"
        
        """
        Metodo que detecta los signos de puntuacions
        
        Args:
            t: token
        """
    
    def t_punto_error(self,t):
        print ("Illegal character '%s'" % t.value[0])
        t.lexer.skip(1)
        
    def t_error(self,t):
        print ("Illegal character '%s'" % t.value[0])
        t.lexer.skip(1)

    def crearDict(self, texto):
        """
        Metodo que comienza el recorrido del texto para obtener un diccionario de
        personajes
        
        Args:
            texto: texto donde buscar los personajes
        """
        txt = ". " + texto
        lex.input(txt)
        for tok in iter(lex.token, None):
            if(tok.value not in self.aux.keys()):
                self.aux[tok.value] = None
                self.mod.anadirPersonaje(tok.value, tok.value)
    