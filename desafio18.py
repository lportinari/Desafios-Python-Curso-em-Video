"""
Exercício Python 018: Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente
desse ângulo.
"""

import math
a = int(input('Digite aqui o ângulo para saber o valor do seno, cosseno e tangente: '))
s = math.sin(math.radians(a))
c = math.cos(math.radians(a))
t = math.tan(math.radians(a))
print('O Ângulo de {:.2f} graus apresenta:'.format(a))
print('Seno: {:.2f}'.format(s))
print('Cosseno: {:.2f}'.format(c))
print('Tangente: {:.2f}'.format(t))

