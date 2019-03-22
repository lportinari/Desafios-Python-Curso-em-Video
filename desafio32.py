"""
Exercício Python 032: Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
"""

from datetime import date
print('*BENVINDO AO IDENTIFICADOR DE ANO BISSEXTO*')
ano = int(input('Digite o ano que quer analisar. Ou digite 0 para analisar o ano atual: '))
if ano == 0:
    ano = date.today().year #Aqui foi aplicado a biblioteca datetime
if ano %4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é Bissexto!'.format(ano))
else:
    print('O ano {} não é bissexto!'.format(ano))
