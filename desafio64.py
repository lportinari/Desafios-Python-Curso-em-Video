"""
Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar
999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles
(desconsiderando o flag).
"""

print('-=' * 15)
print('SOMADOR DE NUMEROS INTEIROS')
print('-=' * 15)
print('Quando quiser encerrar digite 999')
cont = -1
n = 0
n1 = 0
y = 0
while y != 999:
    n = int(input('Digite um valor: '))
    if n == 999:
        y = n
        n = 0
    cont += 1
    n = n + n1
    n1 = n
print('Ao todo foram digitados {} números e a soma entre eles é {}!'.format(cont, n))



