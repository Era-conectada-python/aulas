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
    def __init__(self):
        self.cedulas = [100, 50, 20, 10]

    def saque(self, valor_saque, cliente):
        if valor_saque <= cliente.saldo:
            return True
        return False

    def valida_saque(self, valor_saque): 
        if valor_saque % 10 == 0:
            return True 
        elif valor_saque == float("inf"):
            return True
        return False 

    def valida_cedulas(self, valor_saque):
        if not self.valida_saque(valor_saque):
            return False

        if valor_saque == float("inf"):
            return {100: float("inf"),
                    50: float("inf"),
                    20: float("inf"),
                    10: float("inf")} 

        quantidade_cedulas = {100:0, 50:0, 20:0, 10:0}
        for cedula in self.cedulas:
            quantidade_cedulas[cedula] = valor_saque // cedula

            if valor_saque % cedula == 0:
                return quantidade_cedulas;
            else:
                valor_saque = valor_saque % cedula


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

    def test_valida_saque(self):
        self.assertTrue(self.caixa_eletronico.valida_saque(300))

    def test_valida_saque_invalido(self):
        self.assertFalse(self.caixa_eletronico.valida_saque(57))
       
    def test_valida_saque_infinito(self):
        self.assertTrue(self.caixa_eletronico.valida_saque(float("inf")))

    def test_valida_cedulas_130(self):
        self.assertEqual(self.caixa_eletronico.valida_cedulas(130), {20: 1, 50: 0, 100: 1, 10: 1})

    def test_valida_cedulas_103030(self):
        self.assertEqual(self.caixa_eletronico.valida_cedulas(103030), {20: 1, 50: 0, 100: 1030, 10: 1})

    def test_valida_cedulas_80(self):
        self.assertEqual(self.caixa_eletronico.valida_cedulas(80), {20: 1, 50: 1, 100: 0, 10: 1})

    def test_valida_cedulas_infinito(self):
        self.assertEqual(self.caixa_eletronico.valida_cedulas(float("inf")), {100: float("inf"), 50: float("inf"), 20: float("inf"), 10: float("inf")})

if __name__ == '__main__':
    unittest.main()