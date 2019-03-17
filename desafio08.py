"""
Exercício Python 008: Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
"""

m = float(input('Digite uma distância em metros: '))
c = m * 100
ml = m * 1000
print('{:.2f} metros'.format(m))
print('Centimetros: {:.0f}'.format(c))
print('Milimetros: {:.0f}'.format(ml))



