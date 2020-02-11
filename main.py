# -*- coding: utf-8 -*-

from tst import testUnitarios
from src import Controlador
import unittest

#runner = unittest.TextTestRunner()
#result = runner.run(unittest.makeSuite(testUnitarios.TestUnitarios))

port = int(os.environ.get('PORT', 5000))
Controlador.app.run(threaded=True, host='0.0.0.0', port=port)

