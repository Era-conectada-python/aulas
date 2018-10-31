import unittest

def soma(numero1, numero2):
	return numero1 + numero2

def validador(numero):
	return type(numero) == int

class TestDojoMethods(unittest.TestCase):

    def test_soma(self):
    	self.assertEqual(soma(2,2), 4)

    def test_valida_numero(self):
    	self.assertFalse(validador('x'))


if __name__ == '__main__':
    unittest.main()
