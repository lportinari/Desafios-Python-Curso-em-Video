'''
Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um
dicionário em Python. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.
'''

from random import randint
from time import sleep
from operator import itemgetter
resultados = {}
ranking = []
for j in range(4):
    resultados[f'Jogador{j+1}'] = randint(1, 6)
print('Valores sorteados:')
for k, v in resultados.items():
    sleep(.7)
    print(f'{k} tirou {v} no dado.')
ranking = sorted(resultados.items(), key = itemgetter(1), reverse=True)
print('-=' * 30)
print('   == RANKING DOS JOGADORES ==')
for i, n in enumerate(ranking):
    sleep(.7)
    print(f'    {i+1}º lugar: {n[0]} com {n[1]}.')



