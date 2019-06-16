'''
Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). A primeira função
vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores
pares sorteados pela função anterior.
'''
from random import randint
from time import sleep

numeros = []


def sorteia(lista):
    print('Sorteando 5 valores da lista: ', end='')
    for c in range(5):
        lista.append(randint(1, 10))
        print(lista[c], end=' ')
    print('PRONTO!')
def somaPar(lista):
    soma = 0
    for i in lista:
        if i % 2 == 0:
            soma += i
    print('Somando os valores pares de {}, temos {}'.format(lista, soma))




sorteia(numeros)
somaPar(numeros)