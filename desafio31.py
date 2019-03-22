"""
Exercício Python 031: Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem,
cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.
"""

print('BEM VINDO A CALCULADORA DO VIAJANTE')
d = float(input('Qual a distância da viagem? '))
v = d * 0.5 if d <= 200 else d * 0.45
print('A viagem custará R${:.2f}'.format(v))



