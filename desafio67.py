"""
Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
O programa será interrompido quando o valor digitado for negativo.
"""

print('-=' * 8)
print('Tabuada 3.0')
print('-=' * 8)
while True:
    cont = 0
    print('-' * 35)
    núm = int(input('Quer ver a tabuada de qual valor: '))
    print('-' * 35)
    if núm < 0:
        break
    while cont != 10:
        cont += 1
        produto = núm * cont
        print(f'{núm} x {cont} = {produto}')
print('Programa encerrado. Volte sempre!')



