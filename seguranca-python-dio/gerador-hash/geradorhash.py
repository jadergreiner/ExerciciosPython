import hashlib

texto = input("Digite o texto a ser gerado a hash: \n")

menu = int(input (""" ### MENU - ESCOLHA O TIPO DE HASH
                1) MD5
                2) SHA1
                3) SHA256
                4) SHA512
                Digite o número do hash a ser gerado
        """))

if menu == 1:
    resultado = hashlib.md5(texto.encode('utf-8'))
    print(f'O hash MD5 do texto {texto} é {resultado.hexdigest()}')
elif menu == 2:
    resultado = hashlib.sha1(texto.encode('utf-8'))
    print(f'O hash SHA1 do texto {texto} é {resultado.hexdigest()}')
elif menu == 3:
    resultado = hashlib.sha256(texto.encode('utf-8'))
    print(f'O hash SHA256 do texto {texto} é {resultado.hexdigest()}')    
elif menu == 4:
    resultado = hashlib.sha512(texto.encode('utf-8'))
    print(f'O hash SHA512 do texto {texto} é {resultado.hexdigest()}')
else:
    print("A opção de menu escolhida não é válida")