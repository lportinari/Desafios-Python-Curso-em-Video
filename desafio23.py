"""
Exercício Python 023: Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
"""

print('.:DESCUBRA A UNIDADE, DEZENA, CENTENA E MILHAR DE UM NÚMERO:.')
n = int(input('Digite um número de 0 a 9999: '))
u = n // 1 % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10
#Módulo de cores
cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'verde':'\033[32m',
         'amarelo':'\033[33m',
         'roxo':'\033[35m'}
print('Analisando o número {}'.format(n))
print('{}Unidade{}: {}'.format(cores['azul'], cores['limpa'], u))
print('{}Dezena{}: {}'.format(cores['verde'], cores['limpa'], d))
print('{}Centena{}: {}'.format(cores['amarelo'], cores['limpa'], c))
print('{}Milhar{}: {}'.format(cores['roxo'], cores['limpa'], m))



