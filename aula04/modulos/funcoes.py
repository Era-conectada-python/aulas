def imprimir_nome(n="Sem nome"):
    print(n)

# imprimir_nome("Mário")
# imprimir_nome()

var = 1

def imprimir_numero():
    var = 100
    var2 = 10
    print(var, var2)

def func_test():
    print("test")

def junta_nomes(nome1, nome2="#", nome3="#"):
	return nome1+nome2+nome3


def fat(numero):
	if numero == 0:
		return 1

	return numero * fat(numero-1)

print(fat(0))