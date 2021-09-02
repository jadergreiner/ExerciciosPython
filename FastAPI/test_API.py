import pytest
from requests import get, post
from json import loads

class TestAPI:
    def setup(self):
        self.url = "http://127.0.0.1:8000"

    def test_APIstatus(self):
        resp = get(self.url)
        assert resp.ok

    def test_APIresponde(self):
        resp = get(self.url)
        message = loads(resp.text)
        assert message["message"] == "API para cálculos matemáticos. Informe dois números inteiros e a operação no formato string (somar, subtrair, dividir, multiplicar)"

    def test_POSTsomar(self):
        resp=post(self.url + "/rota"
              , json = {"valor1" : 5, "valor2" : 6, "operacao" : "somar"})
        message = loads(resp.text)
        resposta_esperada = "O resultado da operação é 11"
        assert message == resposta_esperada

    def test_POSTsubtrair(self):
        resp=post(self.url + "/rota"
              , json = {"valor1" : 10, "valor2" : 6, "operacao" : "subtrair"})
        message = loads(resp.text)
        resposta_esperada = "O resultado da operação é 4"
        assert message == resposta_esperada

    def test_POSTdividir(self):
        resp=post(self.url + "/rota"
              , json = {"valor1" : 10, "valor2" : 2, "operacao" : "dividir"})
        message = loads(resp.text)
        resposta_esperada = "O resultado da operação é 5"
        assert message == resposta_esperada

    def test_POSTmultiplicar(self):
        resp=post(self.url + "/rota"
              , json = {"valor1" : 2, "valor2" : 3, "operacao" : "multiplicar"})
        message = loads(resp.text)
        resposta_esperada = "O resultado da operação é 6"
        assert message == resposta_esperada

    def test_POSToperacaoinvalida(self):
        resp=post(self.url + "/rota"
              , json = {"valor1" : 2, "valor2" : 3, "operacao" : "calcula"})
        message = loads(resp.text)
        resposta_esperada = "Os dados informados são inválidos. Informe dois números inteiros e na operação uma das opções (somar, subtrair, dividir, multiplicar)"
        assert message == resposta_esperada
