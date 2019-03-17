"""
Exercício Python 014: Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para
graus Fahrenheit.
"""

t = float(input('Digite a temperatura em Cº: '))
c = 1.8 * t + 32
print('A temperatura {:.1f} Cº covertida em Fahrenheit é {:.1f}Fº'.format(t, c))
