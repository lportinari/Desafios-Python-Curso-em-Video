'''
Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas
 partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em
 um dicionário, incluindo o total de gols feitos durante o campeonato.
'''

jogador = {}
gols = []
total = 0
jogador['Nome'] = str(input('Nome do jogador: '))
partidas = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))
for p in range(partidas):
    gols.append(int(input(f'Quantas gols na partida {p}: ')))
    total += gols[p]
jogador['Gols'] = gols
jogador['Total'] = total
print('-=' * 30)
print(jogador)
print('-=' * 30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}.')
print('-=' * 30)
print(f'O jogador {jogador["Nome"]} jogou {partidas} partidas:')
for i, v in enumerate(jogador['Gols']):
    print(f'    => Na partida {i}, fez {v} gols.')
print(f'Foi um total de {jogador["Total"]} gols em {partidas} partidas!')