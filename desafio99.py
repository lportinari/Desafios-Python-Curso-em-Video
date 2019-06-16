'''
Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. Seu programa
tem que analisar todos os valores e dizer qual deles é o maior.
'''
from time import sleep


def maior(* num):
    maior = 0
    print('-=' * 20)
    print('Analisando os valores passados...')
    for c in num:
        sleep(.7)
        print(c, end=' ', flush=True)
        if c > maior:
            maior = c
    print('foram informados {} valores ao todo'.format(len(num)))
    print('O maior valor informado foi: {}'.format(maior))




maior(2, 4, 6, 7)
maior(5, 1, 9, 2)
maior(6)
maior()
