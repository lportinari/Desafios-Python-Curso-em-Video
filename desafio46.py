"""
Faça um programa que mostre na tela a contagem regressiva para o estouro de fogos de artificio, indo de 10 até 0
, com uma pausa de 1 segundo entre eles.
"""

from time import sleep
import emoji
print('{:=^40}'.format('CONTAGEM REGRESSIVA'))
print('Começa agora a contagem regressiva para o ano de 2018:')
sleep(2)
for c in range(10, -1, -1):
    print(c)
    sleep(1)
print(emoji.emojize(':boom::boom:FELIZ ANO NOVO!!!:boom::boom:', use_aliases=True))
