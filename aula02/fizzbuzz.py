import unittest

# FizzBuzz
# Neste problema, você deverá exibir uma lista de 1 a 100, um em cada linha, com as seguintes exceções:

# Números divisíveis por 3 deve aparecer como 'Fizz' ao invés do número;
# Números divisíveis por 5 devem aparecer como 'Buzz' ao invés do número;
# Números divisíveis por 3 e 5 devem aparecer como 'FizzBuzz' ao invés do número'.

def fizz_buzz():
	lista = criar_lista()
	for numero in lista:
		if check_fizz_buzz(numero):
			print("FizzBuzz")
		elif check_buzz(numero):
			print("Buzz")
		elif check_fizz(numero):
			print("Fizz")
		else:
			print(numero)
	return True

def criar_lista():
	lista = []
	for numero in range(1,101):
		lista.append(numero)
	#print(lista)
	return lista

def check_fizz(numero):
	if numero%3 == 0:
		return True

def check_buzz(numero):
	if numero%5 == 0:
		return True

def check_fizz_buzz(numero):
	if numero%3 == 0 and numero%5 == 0:
		return True

class TestFizzBuzz(unittest.TestCase):

    def teste_principal(self):
    	self.assertTrue(fizz_buzz())

    def test_criar_lista(self):
    	self.assertEqual(len(criar_lista()), 100)

    def test_fizz_por_3(self):
    	self.assertTrue(check_fizz(3))

    def test_fizz_por_9(self):    	
    	self.assertTrue(check_fizz(9))

    def test_buzz_por_5(self):
    	self.assertTrue(check_buzz(5))

    def test_fizz_buzz_15(self):
    	self.assertTrue(check_fizz_buzz(15))


if __name__ == '__main__':
    unittest.main()
