# -*- coding: utf-8 -*-
import csv

class Lectorcsv:
    """
    Clase para importar y exportar diccionarios de personajes
    
    Args:
        m: instancia de la clase modelo
    """
    
    def __init__(self,m):
        self.__modelo = m

    def importDict(self, fichero):
        """
        Metodo que importa un diccionario de personajes que tenga una estructura predeterminada
        
        Args:
            fichero: ruta al fichero csv a importar
        """
        i = 0
        x= True
        with open(fichero, newline='', encoding='utf-8') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=',',skipinitialspace=True)
            for row in spamreader:
                if(x):
                    x = False
                else:
                    if (i%2 ==0):
                        i+=1
                        actual = row[0]
                        self.__modelo.anadirPersonaje(actual,actual)
                    else:
                        i+=1
                        for n in row:
                            self.__modelo.anadirReferenciaPersonaje(actual,n)

    def exportDict(self, fichero):
        """
        Metodo que exporta el diccionario de personajes actual a un fichero csv con una estructura
        igual a la de los ficheros de importación
        
        Args:
            fichero: ruta donde exportar el diccionario
        """
        pers = self.__modelo.getPersonajes()
        with open(fichero, mode='w', newline='', encoding='utf-8') as csvfile:
            spamwriter = csv.writer(csvfile, delimiter=',')
            spamwriter.writerow('Diccionario')
            for persk in pers.keys():
                spamwriter.writerow([persk])
                spamwriter.writerow(pers[persk].getPersonaje().keys())

