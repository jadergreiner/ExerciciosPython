import hashlib

arquivo1 = 'a.txt'
arquivo2 = 'b.txt'


hash1 = hashlib.sha256()

hash1.update(open(arquivo1, 'rb').read())

hash2 = hashlib.sha256()

hash1.update(open(arquivo2, 'rb').read())

if hash1.digest() != hash2.digest():
    print(f'O arquivo: {arquivo1} é diferente do arquivo: {arquivo2}')
    print('O hash do arquivo a.txt é: ', hash1.hexdigest())
    print('O hash do arquivo b.txt é: ', hash2.hexdigest())
else:
    print(f'O arquivo: {arquivo1} é igual ao arquivo: {arquivo2}')
    print('O hash do arquivo a.txt é: ', hash1.hexdigest())
    print('O hash do arquivo b.txt é: ', hash2.hexdigest())