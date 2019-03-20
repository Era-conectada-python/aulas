def soma(numero1, numero2):
    return numero1 + numero2

def validador(numero):
    return type(numero) == int

def test_soma():
    assert soma(2,2) == 4

def test_soma_numero_negativo():
    assert soma(2,-2) == 0, "a função soma() não está somando corretamente números negativos"

def test_valida_numero():
    assert not validador('x')

if __name__ == '__main__':
    test_soma()
    test_soma_numero_negativo()
    test_valida_numero()

# try:
#     10/0
# except ZeroDivisionError:
#     print("divisor igual a zero")
