qtde = 10
class GeraFibo:

    def __iter__(self):
        global qtde
        self.qtde = qtde
        self.var = self.qtde - 2
        self.a1 = 0
        self.a2 = 1
        self.lista = [self.a1, self.a2]

        return self

    def __next__(self):
        proximo = self.a1 + self.a2
        self.lista.append(proximo)
        self.var -= 1
        self.a1 = self.a2
        self.a2 = proximo

        if self.var == 0:
            fibo = {k + 1: v for k, v in enumerate(self.lista)}
            print(fibo)
            raise StopIteration

            return fibo

    def montaFibo():
        gerar = GeraFibo()
        gerar_numeros = iter(gerar)

        for fibo in gerar_numeros:
            print(fibo)

        return gerar_numeros