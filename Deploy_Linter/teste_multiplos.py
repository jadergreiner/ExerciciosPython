import pytest

from multiplos import multiplo5, multiplo7

class TesteMultiplos:
    def setup(self):
        pass

    def test_multiplo5(self):
        resultado = multiplo5(12)

        assert resultado == True

    def test_multiplo7(self):
        resultado = multiplo7(35)

        assert resultado == False
