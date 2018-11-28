import random

arquivo = open("palavras.txt", "r")

palavras = arquivo.readlines()
tam = len(palavras)

for index, palavra in enumerate(palavras):
	palavras[index] = palavra.replace('\n', '')

print(palavras[random.randrange(tam)])