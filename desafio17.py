"""
Exercício Python 017: Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo
retângulo. Calcule e mostre o comprimento da hipotenusa.
"""

import math
a = float(input('Qual o valor do cateto oposto: '))
b = float(input('Qual o valor do cateto adjacente: '))
hi = math.hypot(a, b)
print('O comprimento da hipotenusa é: {:.2f}'.format(hi))

