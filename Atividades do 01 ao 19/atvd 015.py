#conversão de números
print('-' * 70)
num = int(input('Digite um número inteiro: '))
print('-' * 70)
print('''Escolha uma das opções para conversão:
[01] - Converter para Binário
[02] - Converter para Octal
[03] - Converter para Hexadecimal''')
opcao = int(input('Qual é a sua escolha: '))
print('-' * 70)

if opcao == 1:
    print(f'O número {num} convertido para Binário é igual a: {bin(num)[2:]}')
elif opcao == 2:
    print(f'O número {num} convertido para Octal é igual a: {oct(num) [2:]}')
elif opcao == 3:
    print(f'O número {num} convertido para Hexadecimal é igual a: {hex(num)[2:]}')
else:
    print(f'Sua opção é inválida, escolha outro número!')
print('-' * 70)