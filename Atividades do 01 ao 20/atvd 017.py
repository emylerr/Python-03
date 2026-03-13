#IMC
from time import sleep

print('-' * 70)
peso = float(input('Qual é o seu peso (Kg)? '))
altura = float(input('Qual é a sua altura (m)? '))
print('Calculando seu IMC...')
sleep(2)

imc = peso / (altura**2)

print('-' * 70)
if imc <= 18.5:
    print(f'Seu IMC é de {imc:.1f} e você está\033[31m Abaixo do peso.\033[m')
elif imc <= 24.9:
    print(f'Seu IMC é de {imc:.1f} e você está no\033[32m Peso normal.\033[m')
elif imc <= 29.9:
    print(f'Seu IMC é de {imc:.1f} e você está no\033[34m Sobrepeso.\033[m')
elif imc <= 39.9:
    print(f'Seu IMC é de {imc:.1f} e você está no nível de\033[35m Obesidade.\033[m')
    print('Procure um médico! Sua saúde é importante.')
else:
    print(f'Seu IMC é de {imc:.1f} e você está no nível de\033[31m Obesidade mórbida! \033[m')
    print('É necessário um médico\033[31m URGENTE\033[m, sua vida está em risco. ')
print('-' * 70)