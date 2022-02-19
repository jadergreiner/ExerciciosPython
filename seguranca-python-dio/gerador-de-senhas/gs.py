import random, string

tamanho = int(input("Digite o tamanho de dígitos da senha: "))

chars = string.ascii_letters + string.digits + '!@#$%&*()-=+?ç'

rnd = random.SystemRandom()

print(''.join(rnd.choice(chars) for i in range (tamanho)))