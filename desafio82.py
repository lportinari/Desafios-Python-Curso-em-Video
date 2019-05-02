"""Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão
conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três
listas geradas."""

lista = []
par = []
imp = []
while True:
    n = int(input('Digite um número: '))
    lista.append(n)
    if n % 2 == 0:
        par.append(n)
    else:
        imp.append(n)
    resp = str(input('Quer continuar? [S/N]: ')).strip()[0]
    if resp in 'nN':
        break
print('A lista completa é:', lista)
print('A lista de pares é:', par)
print('A lista de ípares é:', imp)