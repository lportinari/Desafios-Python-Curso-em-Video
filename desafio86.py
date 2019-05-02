"""
Crie um programa que declare uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado.
No final, mostre a matriz na tela, com a formatação correta.
"""

matriz = [[], [], []]
for l in range(3):
    for c in range(3):
        matriz[c].append(int(input(f'Digite um valor para [{l},{c}]: ')))
print('-=' * 30)
for l in range(3):
    for c in range(3):
        print('[{:^5}]'.format(matriz[l][c]),end='')
    print()


