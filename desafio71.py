"""
Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será
o valor a se sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
Obs. Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
"""

print('=' * 25)
print('{:^25}'.format('BANCO CELINSKI'))
print('=' * 25)
saque = int(input('Que valor você quer sacar? R$'))
total = saque
cedulas = 50
cont = 0
while True:
    if total >= cedulas:
        total -= cedulas
        cont += 1
    else:
        if cont > 0:
            print('Total de {} cédulas de R${}.'.format(cont, cedulas))
        if cedulas == 50:
            cedulas = 20
        elif cedulas == 20:
            cedulas = 10
        elif cedulas == 10:
            cedulas = 1
        cont = 0
        if total == 0:
            break

print('-'*20)
print('Volte sempre!')




