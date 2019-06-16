'''
Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do
aproveitamento de cada jogador.
'''

jogador = {}
gols = []
lista = []
total = 0
while True:
    jogador.clear()
    jogador['Nome'] = str(input('Nome do jogador: '))
    partidas = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))
    for g in range(partidas):
        gols.append(int(input(f'     Quantos gols na partida {g}: ')))
        total += gols[g]
    jogador['Gols'] = gols[:]
    jogador['Total'] = total
    gols.clear()
    lista.append(jogador.copy())
    total = 0
    while True:
        resp = str(input('Quer continuar? [S/N]: ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Digite S ou N.')
    if resp == 'N':
        break
print('-=' * 30)
print('Cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-' * 40)
for k, v in enumerate(lista):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-' * 40)
while True:
    dados = int(input('Mostrar dados de qual jogador? (999 para parar): '))
    if dados == 999:
        break
    if dados >= len(lista):
        print(f'ERRO! Não existe jogador com código {dados}!')
    else:
        print(f'== LEVANTAMENTO DO JOGADOR {lista[dados]["Nome"]}:')
        for i, v in enumerate(lista[dados]['Gols']):
            print(f'    Na partida {i+1} fez {v} gols')
    print('-' * 40)
print('<< VOLTE SEMPRE >>')



