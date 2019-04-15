"""
Exercício Python 073: Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de
Futebol, na ordem de colocação. Depois mostre:
a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética.
d) Em que posição está o time da Chapecoense.
"""

times = ('Palmeiras', 'Internacional', 'Flamengo', 'Grêmio', 'São Paulo', 'Atlético', 'Cruzeiro', 'Atlético-PR',
         'Santos', 'Bahia', 'Botafogo', 'Fluminense', 'Corinthians', 'Vasco', 'Sport', 'Ceará', 'Chapecoense',
         'Vitória', 'América-MG', 'Paraná')
print('-='*35)
print(f'Lista de times do Brasileirão: {times}')
print('-='*35)
print('Os 5 primeiros são:', times[:5])
print('-='*35)
print('Os últimos 4 colocados:', times[-4:])
print('-='*35)
print('Times em oredem alfabética: ', sorted(times))
print('-='*35)
print('Posição do Chapecoense:', times.index('Chapecoense')+1)