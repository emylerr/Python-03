#Retas de triângulo.
r1 = float(input("Primeiro segmento: "))
r2 = float(input("Segundo segmento: "))
r3 = float(input("Terceiro segmento: "))

if r1 < r2 + r3 and r2 < r1 + 3 and r3 < r1 + r2:
    print('As retas acima podem se formar um triângulo!')
else:
    print('As retas acima não podem se formar uma reta!')