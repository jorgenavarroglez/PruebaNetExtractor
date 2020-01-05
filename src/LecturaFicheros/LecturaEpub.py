# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import zipfile
import re

class LecturaEpub:
    """
    Clase para obtener el texto de los epubs
    
    Args:
        fichero: ruta al fichero epub
    """
    
    def __init__(self,fichero):
        self.fich = fichero
        self.epub = zipfile.ZipFile(self.fich)
        self.__orden = list()
#        print(self.epub.namelist())
    
    def __obtenerOrdenLectura(self):
        """
        Obtiene el orden de lectura en el que se deben leer los ficheros de 
        un archivo epub
        
        Args:
            
        """
        container = self.epub.read('META-INF/container.xml')
        conta = BeautifulSoup(container, "xml")
        for link in conta.find_all('rootfile'):
            content = link.get('full-path')
        carp = re.compile('.*/')
        d = carp.match(content)
        if(d!=None):
            d = d.group()
        else:
            d = ''
            
        content = self.epub.read(content)
        conte = BeautifulSoup(content, "xml")
#        print(conte)
        ordenid = list()
        
        for link in conte.find_all('spine', limit = 1):
            for l2 in link.find_all('itemref'):
                ordenid.append(l2.get('idref'))
        for idr in ordenid:
            for idr2 in conte.find_all(id=idr, limit = 1):
                self.__orden.append(d + idr2.get('href'))
    
    def siguienteArchivo(self):
        """
        Iterador que devuelve el texto de cada fichero a leer del epub
        
        Args:
            
        Yield:
            texto de cada capitulo
        """
        self.__obtenerOrdenLectura()
        for a in self.__orden:
            txt = ''
            if(a in self.epub.namelist()):
                seccion = self.epub.read(a)
                sect = BeautifulSoup(seccion, "xml")
                for s in sect.find_all('p'):
                    txt = txt + s.get_text()+ ". "
                yield txt
