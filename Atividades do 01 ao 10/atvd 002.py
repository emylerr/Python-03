#Velocidade de um veículo
vel = float(input('Qual é a velocidade de ultrapassagem do veículo? '))
aum = vel - 80
multa = 7
multa = aum * multa
if vel > 80:
    print(f'Você ultrapassou a {vel}Km/h e foi multado')
    print(f'Sua multa é de: R${multa:.2f}')
else:
    print('Você está dentro do limite!')
