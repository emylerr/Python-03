#Exército
from datetime import date
atual = date.today().year
data = int(input('Digite seu ano de nascimento: '))

idade = atual - data
idade2 = 18 - idade
idade3 = idade - 18
ano = atual + idade2
ano2 = atual - idade3

print('-' * 70)
print(f'Quem nasceu {data} tem {idade} anos em {atual}.')

if idade == 18:
    print(f'Você já tem {idade} anos, tem que se alistar o mais rápido possível!')
elif idade < 18:
    print(f'Você tem {idade} anos, ainda faltam {idade2} para seu alistamento.')
    print(f'Seu alistamento será em {ano}.')
else:
    print(f'Você já deveria ter se alistado há {idade3} anos.')
    print(f'Seu alistamento foi em {ano2}.')
print('-' * 70)