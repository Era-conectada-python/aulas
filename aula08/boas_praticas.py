# import numpy as np
# np = numpy

lista1 = [1,2,3]

lista2 = list(lista1)

print(lista2, lista1)
print(lista1 == lista2)
print(lista1 is lista2)

lista1.append(10)

print(lista2, lista1)
print(lista1 == lista2)
print(lista1 is lista2)


def soma(num1, num2):
    return num2 + num1

class Calculadora():
    def soma(self, num1, num2):
        return num2 + num1

print(soma(1,2))

calc = Calculadora()
print(calc.soma(1,3))






        






