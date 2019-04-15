"""
Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já
exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem
crescente.
"""

nex = ''
lista = []
while True:
    n = int(input('Digite um valor: '))
    if n not in lista:
        lista.append(n)
        print('Valor adicionado com sucesso')
    else:
        print('Valor duplicado! Não vou adicionar...')
    nex = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
    while nex not in 'SN':
        print('Caractere desconhecido. Digite S para sim ou N para não...')
        nex = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
    if nex == 'N':
         break
lista.sort()
print('-='*30)
print('Você difitou os valores:', lista)

