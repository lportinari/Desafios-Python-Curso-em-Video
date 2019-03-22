"""
Exercício Python 033: Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
"""

print('-=-' * 20)
print('Digite três números e saiba qual o maior e menor valor')
print('-=-' * 20)
a = (int(input('Digite o primeiro Valor: ')))
b = (int(input('Digite o segundo valor: ')))
c = (int(input('Digite o terceiro valor: ')))
maior = a
menor = a
#Verificando quem é maior:
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
#Verificando quem é menor:
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
print('O maior valor digitado é {}'.format(maior))
print('O menor valor digitado é {}'.format(menor))