"""
Exercício Python 030: Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.
"""

print('-=-' * 10) #Apenas enfeite
print('::PROGRAMA PAR OU IMPAR::')
print('-=-' * 10)
x = int(input('Digite um número para saber se ele é par ou ímpar: '))
if x %2 ==0: #Para descobrir se é par ou impar, basta fazer o resto da divisão por 2, se sobrar 0 é par.
    print('O número {} é PAR!'.format(x))
else:
    print('O número {} é ÍMPAR!'.format(x))
