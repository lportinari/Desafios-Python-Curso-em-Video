"""
Faça um programa que ajude um jogador da MEGA SENA a criar palpites.O programa vai perguntar quantos jogos serão gerados
e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
"""

from random import randint
from time import sleep
lista_jogos = []
cont = 0
print('=' * 30)
print('{:^30}'.format('SORTEIO MEGA SENA'))
print('=' * 30)
jogos = int(input('Quantos jogos quer que eu sorteie? '))
for j in range(jogos):
    lista_jogos.append(list())
print('-=' * 3 + ' <SORTEANDO {} JOGOS> '.format(len(lista_jogos)) + '=-' * 3)
for s in range(len(lista_jogos)):
    while True:
        sorteio = randint(1, 60)
        if sorteio not in lista_jogos[s]:
            lista_jogos[s].append(sorteio)
            cont += 1
        if cont == 6:
            break
    cont = 0
    sleep(.8)
    print(f'Jogo {s+1}: {sorted(lista_jogos[s])}')


