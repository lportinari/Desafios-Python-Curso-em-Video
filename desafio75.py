"""
Exercício Python 075: Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla.
No final, mostre:

A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares.
"""

num = (int(input('Digite um número: ')), int(input('Digite outro número: ')), int(input('Digite mais um número: ')),
       int(input('Digite o último número: ', )))
print(f'O valor 9 apareceu {num.count(9)} vezes')
if 3 not in num:
    print('O número 3 não foi digitado')
else:
    print(f'O valor 3 foi digitado na {num.index(3)+1}ª posição')
print('Os números pares foram: ', end='')
for par in num:
    if par % 2 == 0:
        print(f'{par}',end=' ')