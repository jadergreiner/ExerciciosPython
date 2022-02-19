import phonenumbers
from phonenumbers import geocoder

phone = input("Digite o telefone no formato: +5551997402661 \n")

phone_number = phonenumbers.parse(phone)

print(geocoder.description_for_number(phone_number, 'pt'))