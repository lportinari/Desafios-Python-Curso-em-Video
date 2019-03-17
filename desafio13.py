"""
Exercício Python 013: Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de
aumento.
"""

#Revisão
s = float(input('Digite o seu salário R$'))
a = (s * 15) / 100
ns = s + a
print('Seu salário era R${:.2f}, com 15% de aumento (R${:.2f}), passa a ser R${:.2f}'.format(s, a, ns))




