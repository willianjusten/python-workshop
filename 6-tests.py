# coding: utf-8

"""
    assert: permite fazer os próprios asserts
    assertEqual(a, b): verifica se a é igual a b
    assertNotEqual(a, b): verifica se a não é igual a b
    assertIn(a, b): verifica se a existe em b
    assertNotIn(a, b): verifica se a não existe em b
    assertFalse(a): verifica se o valor é False
    assertTrue(a): verifica se o valor é True
    assertIsInstance(a, TYPE): verifica o tipo da variável
    assertRaises(ERROR, a, args): verifica se quando a é chamado sobe um erro
"""

# primeiro importamos o módulo de testes
import unittest

#depois criamos a classe que vai realizar os testes
class Testing(unittest.TestCase):
    # definimos os métodos de teste sempre começando com a palavra
    # test_
    def test_upper(self):
        # usamos então os diferentes tipos de asserts para testar
        self.assertEqual('foo'.upper(), 'FOO')

    def test_soma(self):
        self.assertEqual(2+2, 4)

    def test_soma_errada(self):
        self.assertNotEqual(2*3, 8)

    def test_acha_palavra(self):
        self.assertIn('will', 'will é um péssimo professor')

    def test_acha_palavra(self):
        self.assertIn('willian', 'will é um péssimo professor')

# mandamos rodar o método de unittest
unittest.main()
