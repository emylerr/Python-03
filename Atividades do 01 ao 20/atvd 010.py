#Empréstimo
import emoji
emp = str(input('Bem-vindo ao Banco, deseja simular um financiamento imobiliário? '))
valor = float(input('Qual será o valor do imóvel? R$'))
salario = float(input('Qual é o valor do seu rendimento? R$'))
tempo = int(input('Em quantos anos você pretende quitar sua divída? ' ))
print('-' * 70)

prestacao = valor / (tempo * 12)
limite = salario * 0.30

print(f'Para pagar uma casa de R${valor:.2f}, em {tempo} anos, a prestação será de R${prestacao:.3f}')

if prestacao <= limite:
    print('Seu financiamento imobiliário foi liberado \u2705')
else:
    print('Seu financiamento não foi aprovado! \u274C')
print('-' * 70)
