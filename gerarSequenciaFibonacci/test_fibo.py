import pytest

'''
    Diego, como não consegui usar os metodos de self e iter no teste, modiquei o arquivo para testar
    aqui e demonstrar o que compreendi no pyteste
    
    Defini manualmente a quantidade no arquivo do class e criei uma função a parte para usar aqui no teste
    
    No teste eu verifico se o objeto criado existe 
'''
from classGeraFibo2 import *

class TesteFibo:
    def setup(self):
        pass

    def test_fiboexiste(self):
        resultado = GeraFibo.montaFibo()

        assert resultado != None