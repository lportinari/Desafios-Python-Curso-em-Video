"""
Exercício Python 029: Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma
mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.
"""

v = float(input('Qual a velocidade do carro? '))
c = (v - 80) * 7
if v > int(80):
    print('''MULTADO, você excedeu o limite de velocidade que é 80km/h.
 Você deve pagar uma multa de RS{:.2f}!
 DIRIJA COM CUIDADO!'''.format(c))
else: print('Tenha um ótima viagem!')