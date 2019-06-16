'''
Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo.
Seu programa tem que realizar três contagens através da função criada:

a) de 1 até 10, de 1 em 1
b) de 10 até 0, de 2 em 2
c) uma contagem personalizada
'''

from time import sleep

def contador(i, f, p):
    for c in range(i, f+p, p):
        sleep(.5)
        print(c, end=' ', flush=True)
    print('Fim!')


print('-=' * 20)
print('Contagem de 1 até 10 de 1 em 1: ')
contador(1, 11, 1)
print('-=' * 20)
print('Contagem de 10 até 0 contando de 2 em 2:')
contador(10, 0, -2)
print('-=' * 20)
print('Agora é sua vez de personalizar a contagem.')
inicio = int(input('INICIO: '))
fim = int(input('FIM: '))
passo = int(input('PASSO: '))
contador(inicio, fim, passo)
