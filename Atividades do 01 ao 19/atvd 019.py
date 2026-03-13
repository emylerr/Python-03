#Jogo de pedra, papel e tesoura
from random import randint

print('-' * 35)
print('PEDRA, PAPEL E TESOURA')
print("""Escolha sua opção: 
[0] - Pedra \U0001F44A
[1] - Papel \U0001F590
[2] - Tesoura \U0000270C""")
opcao = int(input('Qual sua jogada? '))
print('-' * 25)

itens = ('Pedra \U0001F44A', 'Papel \U0001F590', 'Tesoura \U0000270C')
comp = randint(0, 2)
print(f'O computador jogou: {itens[comp]}')
print(f'E você jogou: {itens[opcao]}')

if comp == 0:
    if opcao == 0:
        print('Você e a máquina\033[33m EMPATARAM!\033[m \U0001F91D')
    elif opcao == 1:
        print(f'Você\033[32m VENCEU!!!\033[m \U0001F3C6')
    elif opcao == 2:
        print(f'Você\033[31m PERDEU!!!\033[m\U0001F44E')
    else:
        print('Jogada inválida, volte ao inicío.')
elif comp == 1:
    if opcao == 0:
        print(f'Você\033[31m PERDEU!!!\033[m\U0001F44E')
    elif opcao == 1:
        print(f'Você e a máquina\033[33m EMPATARAM!\033[m\U0001F91D')
    elif opcao == 2:
        print(f'Você\033[32m VENCEU!!!\033[m\U0001F3C6')
    else:
        print('Jogada inválida, volte ao inicío.')
elif comp == 2:
    if opcao == 0:
        print(f'Você\033[32m VENCEU!!!\033[m\U0001F3C6')
    elif opcao == 1:
        print(f'Você\033[31m PERDEU!!!\033[m\U0001F44E')
    elif opcao == 2:
        print(f'Você e a máquina\033[33m EMPATARAM!\033[m\U0001F91D')
    else:
        print('Jogada inválida, volte ao inicío.')
print('-' * 25)

#arrumar o inválido