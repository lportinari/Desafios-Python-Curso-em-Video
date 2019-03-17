"""
Exercício Python 011: Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a
quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.
"""

l = float(input('Qual a largura em metros? '))
a = float(input('Qual a altura em metros? '))
area = l * a
tinta = area / 2
print('Sua parede tem a dimensão de {}x{}, sua área é de {:.2f}m² e a quantidade de tinta necessária para pintar '
      'é {:.2f} litros(s)'.format(l, a, area, tinta))





