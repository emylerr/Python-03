#Pagamentos
from time import sleep

print('-' * 70)
compras = float(input('Informe o valor das suas compras: R$'))
print('Escolha uma forma de pagamento: ')
sleep(0.5)

print('''[1] - à vista dinheiro/cheque ou débito
[2] - à vista cartão de crédito
[3] - 2x no cartão de crédito
[4] - 3x ou mais no cartão de crédito''')
opcao = int(input('Qual é a opção? '))


if opcao == 1:
    total = compras - (compras * 10 / 100)
elif opcao == 2:
    total = compras - (compras * 5 / 100)
elif opcao == 3:
    total = compras
    parcelas = total / 2
    print(f'Sua compra será parcelada em 2x de R${parcelas:.2f}')
else:
    total = compras + (compras * 20 / 100)
    totparcelas = int(input('Deseja parcelar em quantas vezes? '))
    parcela = total / totparcelas
    print('-' * 70)
    print(f'Sua compra será parcelada em {totparcelas}x e custará R${parcela}')
print(f'Sua compra no valor de R${compras:.2f} irá custar R${total:.2f} com 20% de juros.')
print('-' * 70)