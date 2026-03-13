#Segmentos de triângulos
print('-' * 70)
r1 = float (input('Primeiro segmento: '))
r2 = float (input('Segundo segmento: '))
r3 = float (input('Terceiro segmento: '))
print('-' * 70)

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print(f'Os segmentos acima podem formar um triângulo', end=' ')
    if r1 ==  r2 == r3:
        print(f'Equilátero.')
    elif r1 != r2 != r3 != r1:
            print(f'Escaleno.')
    else:
        print(f'Isóceles.')
else:
    print(f'Os segmentos acima não podem formar um triângulo.')
print('-' * 70)