"""
Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves.
"""

dados = list()
lista = list()
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    lista.append(dados[:])
    dados.clear()
    resp = str(input('Quer continuar? [S/N]: ')).strip()[0]
    if resp in 'nN':
        break
print(lista)