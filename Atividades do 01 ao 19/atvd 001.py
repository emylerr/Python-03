#Jogo de adivinhar
import random
from time import sleep
n = int(input('Qual foi o número que o computador pensou? '))
num = random.randint(0, 5)
print('Pensando...')
sleep(2)
print(f'O número escolhido foi {num}.')

if n == num:
    print('Parabéns, você venceu!')
else:
    print('Tente novamente!')