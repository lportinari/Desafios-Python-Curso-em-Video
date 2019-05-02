"""
Aprimore o desafio anterior, mostrando no final:
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha.
"""

matriz = [[], [], []]
par = soma = maior = 0
for l in range(3):
    for c in range(3):
        matriz[c].append(int(input(f'Digite um valor para [{l},{c}]: ')))
print('-=' * 30)
for l in range(3):
    for c in range(3):
        print(f'[{matriz[l][c]:^5}]', end='')
        if matriz[l][c] % 2 == 0:
            par += matriz[l][c]
    print()
print(f'A soma dos valores pares é {par}')
for c in range(3):
    soma += matriz[c][2]
print(f'A soma dos valores da terceira coluna é {soma}')
for l in range(3):
    if matriz[1][l] > maior:
        maior = matriz[1][l]
print(f'O maior valor da segunda linha é {maior}')