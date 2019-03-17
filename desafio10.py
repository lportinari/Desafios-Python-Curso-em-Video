"""
Exercício Python 010: Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares
ela pode comprar.
"""

r = float(input('Nos diga quanto tem em sua carteira e saiba quantos doláres pode comprar: '))
d = r / 3.27
print('Com R${:.2f} você pode comprar Us${:.2f}'.format(r, d))
