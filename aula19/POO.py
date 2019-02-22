from abc import ABC, abstractmethod

class Animal(ABC):
	def __init__(self, nome):
		self.nome = nome

	@abstractmethod
	def emitir_som(self):
		pass

class Cachorro(Animal):
	def emitir_som(self):
		print("Au au")

class Gato(Animal):
	def emitir_som(self):
		print("Miau")

class Lesma(Animal):
	def rasteja(self):
		pass

	def emitir_som(self):
		print("...")

rex = Cachorro('Rex')
rex.emitir_som()

mimi = Gato('Mimi')
mimi.emitir_som()

alfred = Lesma('Alfred')
alfred.rasteja()

