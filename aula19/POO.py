from abc import ABC, abstractmethod

class Animal(ABC):
	def __init__(self, nome):
		self.nome = nome
		self.__apelido = "Meu nome é: "+nome

	@abstractmethod
	def emitir_som(self):
		pass

class Produto():
	def get_value(self):
		print('R$ 10')


class Cachorro(Animal, Produto):
	def emitir_som(self):
		print("Au au")

class Gato(Animal):
	def emitir_som(self):
		print("Miau")

class Lesma(Animal):
	def __rasteja(self):
		pass

	def fugir(self):
		self.__rasteja()
		print('fuga!')

	def emitir_som(self):
		print("...")

rex = Cachorro('Rex')
print(rex.nome, rex.get_value())
rex.emitir_som()

mimi = Gato('Mimi')
mimi.emitir_som()

alfred = Lesma('Alfred')
alfred.fugir()
# alfred.rasteja()

