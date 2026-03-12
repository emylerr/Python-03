#Aumento de salário
salario = float(input('Digite seu salário: R$'))
aum1 = salario * 0.10
aum2 = salario * 0.15

if salario < 1.250:
    print(f'Seu salário é de R${salario} e seu aumento é de 10%! O seu novo salário irá para R${aum1 + salario:.2f}')
else:
    print(f'Seu salário é de R${salario} e seu aumento é de 15%! O seu novo salário irá para R${aum2 + salario:.2f}')