import random

arquivo = open("palavras.txt", "r")

palavras = arquivo.readlines()
tam = len(palavras)

for index, palavra in enumerate(palavras):
	palavras[index] = palavra.replace('\n', '')

palavra = palavras[random.randrange(tam)]

fim = False
palavra_completa = False
erros = 0
palavra_forca = []

for x in palavra:
	palavra_forca.append("_")

while not fim:
	letra = input('Digite uma letra: ')

	if len(letra) > 1 and letra != palavra:
		erros += 1
		print("Você errou pela {0}ª vez. Tente de novo!".format(erros))
	elif len(letra) > 1 and letra == palavra:
		fim = True
		print('A palavra é : {0}'.format(letra))
		print("Ganhou!")
	elif letra in palavra:
		for index, l in enumerate(palavra):
			if l == letra:
				palavra_forca[index] = l

		if not '_' in palavra_forca:
			print('A palavra é : {0}'.format(''.join(palavra_forca)))
			palavra_completa = True
		else:
			print('A palavra é : {0}'.format(' '.join(palavra_forca)))
	else:
		erros += 1
		print("Você errou pela {0}ª vez. Tente de novo!".format(erros))

	if erros == 6:
		fim = True
		print("Game Over")
	elif palavra_completa:
		fim = True
		print("Ganhou!")