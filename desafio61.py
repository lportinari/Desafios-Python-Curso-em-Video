"""Refaça o desafio 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da
progeressão usando a estrutura while."""

termo = int(input('Digite o primeiro termo: '))
razão = int(input('Digite a razão: '))
contador = termo + (10 - 1) * razão
c = 0
n = 10
print('Segue abaixo os primeiros termos da P.A de razão {}, sendo o primeiro termo {}'.format(razão, termo))
while c != contador:
    c = termo + (10 - n) * razão
    n = n - 1
    print(c,end=', ' if c != contador else '...')
print('Fim')



