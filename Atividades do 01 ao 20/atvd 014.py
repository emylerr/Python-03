#Idade e sua categoria
from datetime import date
import random

print('-' * 70)
print('Bem-vindo a Confederação Nacional de Natação', end='. ')
print('Insira seus dados abaixo: ')

ano = date.today().year
nome = str(input('Qual é o seu nome completo? '))
nasc = int(input('Qual é o ano do seu nascimento? '))

idade = ano - nasc

print('-' * 70)
print(f'Bem-vindo(a) {nome.title()}, sua idade é {idade} anos em {ano}.')

if idade <= 9:
    print(f'Você tem {idade} anos, e sua categoria é\033[36m MIRIM \033[m')
elif idade <= 14:
    print(f'Você tem {idade} anos, e sua categoria é\033[33m INFANTIL \033[m')
elif idade <= 19:
    print(f'Você tem {idade} anos, e sua categoria é\033[35m JUNIOR \033[m')
elif idade <= 20:
    print(f'Você tem {idade} anos, e sua categoria é\033[31m SÊNIOR \033[m')
else:
    print(f'Você tem {idade} anos e sua categoria é\033[30m MASTER \033[m')

print('-' * 70)