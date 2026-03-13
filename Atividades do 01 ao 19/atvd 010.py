#Empréstimo
import emoji
print('-' * 70)
valor = float(input('Qual será o valor do imóvel? R$'))
salario = float(input('Qual é o valor do seu rendimento? R$'))
tempo = int(input('Em quantos anos você pretende quitar sua divída? ' ))
print('-' * 70)

prestacao = valor / (tempo * 12)
limite = salario * 0.30

print(f'Para pagar uma casa de R${valor:.2f}, em {tempo} anos, a prestação será de R${prestacao:.2f}')

if prestacao <= limite:
    print('Seu financiamento imobiliário\033[32m FOI LIBERADO \u2705 \033[m')
else:
    print('Seu financiamento\033[31m NÃO FOI APROVADO \u274C \033[m')
print('-' * 70)