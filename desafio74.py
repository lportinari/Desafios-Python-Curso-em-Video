"""
Exercício Python 074: Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso,
mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.
"""

from random import randint
num = (randint(0,10), randint(0,10), randint(0,10), randint(0,10), randint(0,10))
print('Os valores sorteados foram:', num)
print('O maior número sorteado foi:', max(num))
print('O menor número sorteado foi:', min(num))