import socket
import sys

def main():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    except socket.error as e:
        print("Erro na conexão! Falhou")
        print("Erro: {}" .format(e))
        sys.exit()

    
    print("Socket criado com sucesso")

    HostAlvo = input("Digite o Host ou IP a ser conectado: ")
    PortaAlvo = input("Digite a porta de conexão: ")

    try:
        s.connect((HostAlvo, int(PortaAlvo)))
        print("Cliente TCP conectado com sucesso no Host" + HostAlvo + " na porta " + PortaAlvo)
        s.shutdown(2)
    except socket.error as e:
        print("A conexão falhou.")
        print("Erro: {}" .format(e))
        sys.exit()

if __name__ == "__main__":
    main()