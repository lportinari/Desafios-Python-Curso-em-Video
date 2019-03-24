"""
Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos
dessa progressão.
"""

print('-*' * 11)
print('PROGRESSÃO ARITMÉTICA')
print('-*' * 11)

termo = int(input('Digite o primeiro termo: '))
razão = int(input('Digite a razão: '))
count = termo + (10 - 1) * razão
print('Segue abaixo os 10 primeiros termos da progressão aritmética:')
for c in range(termo, count + 1, razão):
    print(c, end=', ')
print('FIM')


