1.	Faça um programa que imprima seu nome completo na tela
2.	Escreva um programa que exiba o resultado de 5a x 3b onde a = 2 e b = 5
3.	Modifique o programa anterior, inserindo uma terceira variável c = 5 e imprima a soma das três variáveis
4.	Escreva um programa que leia dois números e que pergunte qual operação você deseja realizar. Você deve poder calcular a soma (+), subtração(-), multiplicação(*) e divisão(/). Exiba o resultado da operação.
5.	Escreva um programa para contar de 1 até 10.

a)	usando a instrução while
b)	usando a instrução for e a função range

6.	Escreva um programa para contar quantos números pares e ímpares existentes entre 1 e 10 bem como a soma deles.

a)	usando a instrução while
b)	usando a instrução for e as funções range e sum


7.	Escreva um programa para resolver equações do segundo grau representadas por ax2+bx+c usando a Fórmula de Bhaskara.

a)	sem usar o módulo math
b)	usando o módulo math
c)	Teste seu programa com os coeficientes:

a=1,b=-5,c=6 a=1,b=0,c=-9 a=5,b=-45,c=0 a=1,b=-1,c=-12 a=1,b=-6,c=10

Dica: Você não precisa necessariamente fazer uma entrada dos valores de a, b e c a partir do usuário. Você pode declarar esses valores antes e efetuar o cálculo.

Dica 2: Para importar o módulo math, use o comando import math, assim você poderá usar com mais facilidade funções matemáticas da biblioteca. Para saber mais detalhes, consulte: https://docs.python.org/pt-br/3/library/math.html

8.	Vamos reescrever o programa acima criando uma função bhaskara que recebe como parâmetros os coeficientes a, b e c e retorna as raízes da equação.

Dica: Iremos aprender sobre funções no próximo módulo, fique tranquilo. Contudo, você já pode começar a praticar. A definição da função é a seguinte:

def bhaskara(a, b, c): delta = b ** 2 - 4 * a * c if delta < 0:
 
return None
else:
raizes = []
m1 = math.sqrt(delta) r1 =(-b + m1) / (2 * a) raizes.append(r1)
r2 =(-b - m1) / (2 * a) raizes.append(r2) return raizes

Responda as questões a seguir:
a)	O que significam palavras reservadas em Python? Quais são as palavras reservadas no código acima?
b)	Qual a função de cada uma dessas palavras reservadas no código?
c)	Implemente a função acima e mostre na tela, o resultado da equação de segundo grau.

9.	Considerando a string s = 'Mentorama' escreva um programa que:
a)	converta a string para maiúsculo, em seguida
b)	imprima-a de trás para frente
c)	imprima somente as vogais

10.	Escreva um programa que receba como entrada do usuário o nome “João” sobrenome “da Silva”, idade “25”, Cidade “São Paulo”, ddd “11”, telefone “3333-3333” e faça as seguintes instruções:

a)	imprima na tela o nome completo em uma única linha Nome: João da Silva
b)	imprima na tela o telefone com ddd em uma única linha Telefone: (11)3333-3333
c)	Imprima na tela a idade Idade: 25
d)	Imprima na tela a cidade Cidade: São Paulo


