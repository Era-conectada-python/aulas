import unittest

# Dicionário de idiomas



esp = {1: 'uno', 2: 'dos', 3: 'tres', 4: 'quatro', 5: 'cinco'}
ing = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five'}
por = {1: 'um', 2: 'dois', 3: 'três', 4: 'quatro', 5: 'cinco'}
linguas = {'espanhol': esp, 'inglês': ing, 'português': por}

def check_numero(numero):
    return int == type(numero)

def check_lingua(lingua):
    return lingua in linguas

def check_numero_existente(numero):
    return numero in esp

def numero_extenso(numero, lingua):
    try:
        if not check_numero(numero) or not check_lingua(lingua):
            return False

        return linguas[lingua][numero]

    except:
        
        return False




class TestFizzBuzz(unittest.TestCase):

    def teste_valida_numero(self):
        self.assertTrue(check_numero(2))

    def teste_valida_texto(self):
        self.assertFalse(check_numero('A'))

    def teste_valida_none(self):
        self.assertFalse(check_numero(None))

    def teste_valida_lingua(self):
        self.assertTrue(check_lingua('espanhol')) 

    def teste_valida_lingua(self):
        self.assertFalse(check_lingua('francês')) 

    def teste_valida_numero_existente(self):
        self.assertTrue(check_numero_existente(3))   

    def teste_valida_numero_inexistente(self):
        self.assertFalse(check_numero_existente(10)) 

    def teste_numero_ingles(self):
        self.assertEqual(numero_extenso(2, 'inglês'), 'two')

    def teste_numero_espanhol(self):
        self.assertEqual(numero_extenso(2, 'espanhol'), 'dos')
    
    def teste_numero_portugues(self):
        self.assertEqual(numero_extenso(2, 'português'), 'dois')

    def teste_numero_inexistente(self):
        self.assertFalse(numero_extenso(100, 'português'), 'cem')
    

if __name__ == '__main__':
    unittest.main()
