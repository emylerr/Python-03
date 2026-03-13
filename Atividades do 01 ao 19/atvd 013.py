#Média de aluno
from time import sleep
print('-' * 70)
n1 = float(input('Digite sua 1ª nota: '))
n2 = float(input('Digite sua 2ª nota: '))
media = (n1 + n2) / 2
print('Calculando sua média...')
sleep(2)

print('-' * 70)
if media >= 7.0:
    print(f'Sua média final foi {media:.1f}, você foi\033[32m APROVADO\033[m \u2705')
elif media >= 5.0 and 6.9:
    print(f'Sua média final foi {media:.1f}, você está de\033[33m RECUPERAÇÃO\033[m \u231B')
else:
    print(f'Sua média final foi {media:.1f}, você foi\033[31m REPROVADO\033[m \u274C')
print('-' * 70)

#cód de cores adicionadas: \033[32m (abre cor) \033[m (fecha cor).