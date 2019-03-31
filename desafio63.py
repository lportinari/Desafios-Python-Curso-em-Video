"""
Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros elementos de
uma sequencia Fibonacci.
ex: 0 -> 1 -> 1 -> 2 -> 3 -> 5 -> 8
"""

n = int(input('Quantos termos você quer mostrar: '))
n1 = 0
n2 = 1
cont = 3
print('{} -> {}'.format(n1, n2), end='')
while cont <= n:
    n3 = n1 + n2
    cont += 1
    print(' -> {}'.format(n3), end='')
    n1 = n2
    n2 = n3
print(' -> FIM')




