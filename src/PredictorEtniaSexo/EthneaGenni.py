# -*- coding: utf-8 -*-
import urllib
from bs4 import BeautifulSoup

class EthneaGenni:
    """
    Clase que crea un diccionario de manera automática
    
    Args:
        modusuario: instancia de la clase modelo
    """
    
    def __init__(self):
        self.replacements = (
            ("á", "a"),
            ("é", "e"),
            ("í", "i"),
            ("ó", "o"),
            ("ú", "u"),
            ("#", ""),
            (" ", "+"),
            ("&", "%26"),
            ("ø","o"),
            ("ä", "a"),
            ("ë", "e"),
            ("ï", "i"),
            ("ö", "o"),
            ("ü", "u"),
            ("à", "a"),
            ("è", "e"),
            ("ì", "i"),
            ("ò", "o"),
            ("ù", "u"),
            ("ñ", "n"),
            ("½", "")
            
        )
    
    def normalize(self,s):
        """
        Metodo para eliminar acentos y algunos caracteres especiales en la lectura de la página
        
        Args:
            s: string que se quiere normalizar

        Return:
            el string normalizado
        """
        for a, b in self.replacements:
            s = s.replace(a, b).replace(a.upper(), b.upper())
        return s

    def separaNombres(self, nombre):
        """
        Metodo para separar un único string con nombre y apellido en dos strings individuales
        
        Args:
            nombre: string para separar en dos

        Return:
            firstname: el nombre
            lastname: el apellido
        """
        name = nombre.split(maxsplit=1)
        if len(name) == 1:
            firstname = name[0]
            lastname = name[0]
        else:
            firstname = name[0]
            lastname = name[1]
        return self.normalize(firstname), self.normalize(lastname)
    
    def obtenerEtniaSexo(self, nombre):
        """
        Método para obtener un diccionario de personajes haciendo web scraping
    
        Args:
            url: url donde hacer web scraping
        """
        firstname, lastname = self.separaNombres(nombre)
        url = 'http://abel.lis.illinois.edu/cgi-bin/ethnea/search.py?Fname='+firstname+'&Lname='+lastname+'&format=json'
        web = urllib.request.urlopen(url)
        html = BeautifulSoup(web.read(), "html.parser")
        jsonCosas = str(html)
        ethnia = eval(jsonCosas)['Ethnea']
        sexo = eval(jsonCosas)['Genni']
        first = eval(jsonCosas)['First']
        last = eval(jsonCosas)['Last']
        return ethnia,sexo