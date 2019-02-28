import unittest

# Entregar o menor número de notas;
# É possível sacar o valor solicitado com as notas disponíveis;
# Saldo do cliente infinito;
# Quantidade de notas infinito (pode-se colocar um valor finito de cédulas para aumentar a dificuldade do problema);
# Notas disponíveis de R$ 100,00; R$ 50,00; R$ 20,00 e R$ 10,00

class Cliente:
    def __init__(self, nome, saldo):
        self.nome = nome
        self.saldo = saldo
        
class CaixaEletronico:
    def __init__(self, cedulas):
        self.cedulas = cedulas

    def saque(self, valor_saque, cliente):
        if valor_saque <= cliente.saldo:
            return True
        return False

class DojoPOOMethods(unittest.TestCase):

    def setUp(self):
        self.joao = Cliente("João", float("inf"))
        self.felipe = Cliente("Felipe", 500)
        self.everton = Cliente("Everton", 300)

        self.caixa_eletronico = CaixaEletronico()

    def test_saque_com_saldo(self):
        self.assertTrue(self.caixa_eletronico.saque(50,self.felipe))

    def test_saque_sem_saldo(self):
        self.assertFalse(self.caixa_eletronico.saque(700,self.felipe))

    def test_saque_infi(self):
        self.assertTrue(self.caixa_eletronico.saque(float("inf"),self.joao))

    def test_saque_infi_false(self):
        self.assertFalse(self.caixa_eletronico.saque(float("inf"),self.everton))



if __name__ == '__main__':
    unittest.main()