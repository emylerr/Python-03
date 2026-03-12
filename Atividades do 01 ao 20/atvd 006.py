#Menor número
n1 = float(input('Digite um número: '))
n2 = float(input('Digite um segundo número: '))
n3 = float(input('Digite um terceiro número: '))

if n1 > n2 and n3:
    print(f'O primeiro número é o maior!')
elif n2 > n3 and n1:
    print(f'O segundo número é o maior!')
elif n3 > n2 and n1:
    print(f'O terceiro número é o maior!')
else:
    print('Todos os números são iguais!')
print('-' * 35)