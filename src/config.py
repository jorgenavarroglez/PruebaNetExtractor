# -*- coding: utf-8 -*-
import os
import secrets
#Idiomas permitidos en internacionalización
LANGUAGES = {
    'en': 'English',
    'es': 'Español'
}
#Carpeta donde subir archivos
upload_folder = os.path.join(os.path.dirname(os.path.realpath(__file__)),"ficheros")
#Carpera donde se guardan las traducciones
translations_folder = os.path.join(os.path.dirname(os.path.realpath(__file__)),"translations")
#Clave secreta
secretkey = secrets.token_urlsafe(16)
