#Km rodados
km = float(input('Qual será a distância da sua viagem? '))
km5 = km * 0.50
km4 = km * 0.45

print(f'A passagem ficará no valor de: R${km5}' if km <= 199 else f'Sua viagem é de {km} então  a passagem custará: R${km4} por Km rodados')

'''
Segundo método

if km <= 199:
    print(f'Sua viagem é de {km}Km, então ficará no valor de: R${km5}por Km rodados')
elif km > 200:
    print(f'Sua viagem é de {km}Km, então custará: R${km4} por Km rodados')
'''