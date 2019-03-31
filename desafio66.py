"""
Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar
999, que é a condição de parada. No final, mostre quantos números foram digitados e qual a soma entre eles.
(Desconsiderando o flag)
"""

print('-=' * 12)
print('SOMADOR DE NÚMEROS')
print('-=' * 12)
cont = soma = 0
while True:
    n = int(input('Digite um número (999 para parar): '))
    if n == 999:
        break
    cont += 1
    soma += n
print(f'Ao todo foi digitado {cont} números e a soma entre ele é {soma}.')
