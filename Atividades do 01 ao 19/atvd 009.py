#adicionando cores no terminal
'''tabela:
código: \033[xx;xx;xxm]
style: 0 (nada), 1 (negrito), 4 (italico) e 7 (fundo branco c/ número preto).
text: 30 (cinza), 31 (vermelho), 32 (verde), 33 (amarelo), 34 (azul), 35 (roxo), 36 (ciano) e 37 (branco)
background: mesmas cores porem com 40, 41, 42...
'''
a = 3
b = 5
print(f'\033[37m os valores são \033[32m{a}\033[37m e \033[35m{b}')