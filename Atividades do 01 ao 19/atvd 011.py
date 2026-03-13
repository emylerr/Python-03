#Maior número
n1 = int(input('Digite o 1º número: '))
n2 = int(input('Digite o 2º número: '))

if n1 > n2:
    print(f'O número {n1} é o maior!')
elif n2 > n1:
    print(f'O número {n2} é o maior!')
else:
    print('Os números são idênticos.')