# -*- coding: utf-8 -*-

#from src import personaje
#from tst import TestUnitarios
from src import Controlador
import unittest
import os

#runner = unittest.TextTestRunner()
#result = runner.run(unittest.makeSuite(testUnitarios.testUnitarios))
port = int(os.environ.get('PORT', 5000))
Controlador.app.run(threaded=True, host='0.0.0.0', port=port)