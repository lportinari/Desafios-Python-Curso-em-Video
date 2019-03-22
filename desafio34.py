"""
Exercício Python 034: Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.
"""

print('CÁLCULO DE AUMENTO SALARIAL')
f = float(input('Quanto você ganha? R$'))
s1 = f * 10 /100 + f
s2 = f * 15 / 100 + f
if f > 1250.00:
    print('Parabéns, seu salário com 10% de aumento fica R${:.2f}'.format(s1))
else:
    print('Parabéns, seu salário com 15% de aumento fica R${:.2f}'.format(s2))