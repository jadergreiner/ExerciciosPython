import ipaddress

ip = '192.168.0.1'
ipRede = '162.168.0.0/24'

endereco = ipaddress.ip_address(ip)
rede = ipaddress.ip_network(ipRede)

print(endereco)
print(endereco + 100)
print(endereco + 257)
print(f'ip e rede: {rede}')
