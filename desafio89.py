"""
Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um
boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.
"""

lista = list()
dados = []
media = 0
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Nota 1: ')))
    dados.append(float(input('Nota 2: ')))
    lista.append(dados[:])
    dados.clear()
    next = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
    if next == 'N':
        break
print('-=' * 30)
print('Nº ' + 'Nome' + ' ' * 10 + 'MÉDIA')
print('-' * 25)
for m in range(len(lista)):
    media = (lista[m][1] + lista[m][2]) / 2
    print('{:<2} {:<15} {:.1f}'.format(m, lista[m][0], media))
print('-' * 30)
while True:
    notas = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if notas == 999:
        break
    print(f'Notas de {lista[notas][0]} são [{lista[notas][1]}, {lista[notas][2]}]')
    print('-' * 30)
print('FINALIZANDO...')
print('<<< VOLTE SEMPRE >>>')

