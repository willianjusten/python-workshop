# -*- coding: utf-8 -*-

# Escreva um programa que leia um valor em metros e o
# exiba convertido em milímetros
# Faça com TDD

import unittest

class Testing(unittest.TestCase):
    def test_meters_to_milimeters_zero(self):
        self.assertEqual(meters_to_milimeters(0), 0)

    def test_meters_to_milimeters_com_valor(self):
        self.assertEqual(meters_to_milimeters(1), 100)

unittest.main()