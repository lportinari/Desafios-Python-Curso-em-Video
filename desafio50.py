"""
Desenvolva um programa que leia 6 números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor
digitado for ímpar, desconsidere-o.
"""

print('|' * 25)
print('SOMADOR DE NUMEROS PARES')
print('|' * 25)
soma = 0
count= 0
for c in range(1, 7):
    n = int(input('Digite o {}º valor: '.format(c)))
    if n % 2 == 0:
        soma += n
        count += 1
print('A soma dos números pares é {}.'.format(soma))
print('Foi encontrado ao todo {} número(s) par(es).'.format(count))


