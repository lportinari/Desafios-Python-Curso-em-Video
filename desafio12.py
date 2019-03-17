"""
Exercício Python 012: Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
"""
print('-=-' * 12)
print('BEM VINDO AO PROGRAMA DE DESCONTOS')
print('-=-' * 12)
p = float(input('Digite o valor do produto: R$'))
d = (p * 5) / 100
np = p - d
print('O produto custa R${:.2f}, com o desconto de 5% (R${:.2f}), o produto passa a valer R${:.2f}'.format(p, d, np))
