# Função para testar se os numbers são multiplies de 5 ou 7
def multiplo5(numero):
    """
    Função que verifica os multiplos de 5
    """
    if numero % 5 == 0:
        mult5 = True
    else:
        mult5 = False
    return mult5


def multiplo7(numero):
    """
    Função que verifica os multiplos de 7
    """
    if numero % 7 == 0:
        mult7 = True
    else:
        mult7 = False
    return mult7
