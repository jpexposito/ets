#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from programa import Calculadora


"""
Ejemplos de Test utilizando la libreria unittest
"""
class TestMyModule(unittest.TestCase):
    
    def test_sum(self):
        cal = Calculadora(5, 7)
        resultado = cal.sum()
        self.assertEqual(resultado, 12, "No se ha obtenido el resultado esperado")


if __name__ == "__main__":
    unittest.main()