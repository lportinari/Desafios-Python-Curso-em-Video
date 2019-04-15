"""
Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor
valor digitado e as suas respectivas posições na lista
"""

lista = list()
maior = menor = 0
for item in range(5):
    lista.append(int(input(f'Digite um valor na posição {item}: ')))
    if item == 0:
        maior = lista[item]
        menor = lista[item]
    else:
        if lista[item] > maior:
            maior = lista[item]
        if lista[item] < menor:
            menor = lista[item]
print(f'Você digitou os valores {lista}')
print(f'O maior valor digitado foi {maior} nas posições', end=' ')
for i, v in enumerate(lista):
    if v == maior:
        print(i, end=' ')
print()
print(f'O menor valor digitado foi {menor} nas posições', end=' ')
for i, v in enumerate(lista):
    if v == menor:
        print(i, end=' ')