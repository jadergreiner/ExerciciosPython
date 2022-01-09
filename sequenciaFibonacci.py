'''

A seguinte sequência de números 0 1 1 2 3 5 8 13 21... é conhecida como série de Fibonacci. Nessa sequência, cada número, depois dos 2 primeiros, é igual à soma dos 2 anteriores. Escreva um algoritmo que leia um inteiro N (N < 46) e mostre os N primeiros números dessa série.

Entrada
O arquivo de entrada contém um valor inteiro N (0 < N < 46).

Saída
Os valores devem ser mostrados na mesma linha, separados por um espaço em branco. Não deve haver espaço após o último valor.

'''

n = int(input('Inserir numero para gerar a sequência de Fibonnaci :'))

u_1 = 1
u_2 = 1
count = 0

lista = [0,1,1]

seq = n -3


for vic in range(0, seq):
    count = u_1 + u_2
    u_1 = count
    u_2 = (count - u_2)
    lista.append(count)

if n == 2:
    print ("0 1")    
else:
    print(' '.join(map(str, lista)))
