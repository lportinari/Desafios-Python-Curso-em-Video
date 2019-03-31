"""
Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre
todos os valores e qual foi o maior e o menor valor lido. O programa deve perguntar ao usuário se ele quer ou
não continuar a digitar valores.
"""

cont = soma = média = maior = menor = 0
resp = 'S'
while resp in 'Ss':
    núm = int(input('Digite um número: '))
    cont += 1
    soma += núm
    if cont == 1:
        maior = menor = núm
    else:
        if núm > maior:
            maior = núm
        if núm < menor:
            menor = núm
    resp = str(input('Quer continuar [S/N]: ')).upper().split()[0]
média = soma / cont
print('Você digitou {} números e a média foi {}!'.format(cont, média))
print('O maior número foi {} e o menor foi {}!'.format(maior, menor))


