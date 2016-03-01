# coding: utf-8
# 
# Faça um programa, que peça do usuário o valor da conta do restaurante
# e retorne o total a pagar
# Faça usando TDD!

import unittest

def conta(num):
    return int(num * 1.1)

class Testing(unittest.TestCase):
    def test_conta_zerada(self):
        self.assertEqual(conta(0), 0)

    def test_conta_com_valor(self):
        self.assertEqual(conta(100), 110)

unittest.main()