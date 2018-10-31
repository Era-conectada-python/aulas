# Aula inical de Python
# Versão 3.*

#Variáveis

nome = 'Mário Sérgio'
type(nome) # tipo str

numero = 10
type(numero) # tipo int

verdadeiro = True
type(verdadeiro) # tipo bool

#imprimir todas as variáveis acima
print(nome, numero, verdadeiro)


#Listas
lista = [0,1,2,3,4,5,6,7,8,9,10]
print(lista)

#imprimir o primeiro elemento de uma lista
print(lista[0])

#imprimir o último elemento de uma lista
print(lista[-1])

# O comando asseguir adiciona um elemento no final da lista
lista.append('numero')

# O comando asseguir adiciona um elemento em uma posição específica da lista
lista.insert(3, 'PYTHON')

dicionario = {'nome': 'Mário', 'idade': 25}

print(dicionario['nome'])

