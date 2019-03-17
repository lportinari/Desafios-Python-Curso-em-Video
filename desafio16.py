"""
Exercício Python 016: Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção
Inteira.
"""

from math import trunc
n = float(input('Digite um número real e saiba a sua porção inteira: '))
print('O numero digitado foi {} e a sua parte inteira é:'.format(n), trunc(n))


