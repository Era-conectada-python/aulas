matriz = [[1, 2, 5], [2, 4, 10], [0, 2, -6]]
# print(matriz)

# for index, valor in enumerate(matriz):
# 	for i, numero in enumerate(valor):
# 		matriz[index][i] = numero**2

# List Comprehensions
matriz = [[value**2 for value in line] for line in matriz]

# print(matriz)

# squares = [x**2 for x in range(10)]
# print(squares)

lista = [1,2,3,4,5,6]
# [value*10 if value > 3 else value**2 for value in lista]

for index, value in enumerate(lista):
	if value > 3:
		lista[index] = value*10
	else:
		lista[index] = value**2
print(lista)