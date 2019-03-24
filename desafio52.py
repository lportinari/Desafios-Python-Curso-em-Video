"""
Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
"""

print('=' * 31)
print('IDENTIFICADOR DE NÚMEROS PRIMOS')
print('=' * 31)

num = int(input('Digite um número: '))
total = 0
for c in range(1, num+1):
    if num % c == 0:
        print('\033[0;36m', end='')
        total += 1
    else:
        print('\033[0;31m', end='')
    print('{}'.format(c), end=' ')
print('\n\033[mO número {} foi divisível {} vezez.'.format(num, total))
if total == 2:
    print('E por isso ele É PRIMO')
else:
    print('E por isso ele NÃO É PRIMO')



