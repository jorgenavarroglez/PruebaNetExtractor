# -*- coding: utf-8 -*-

from tst import testUnitarios
from src import Controlador
import unittest

#runner = unittest.TextTestRunner()
#result = runner.run(unittest.makeSuite(testUnitarios.testUnitarios))

Controlador.app.run(threaded=True, debug=True)

