"""
Crie um programa que leia o nome e o preço de vários produtos. o programa deverá perguntar se o usuário vai
continuar. No final, mostre:
1 - Qual é o total gasto na compra.
2 - Quantos produtos custam mais de R$1000,00.
3 - Qual o nome do produto mais barato.
"""

print('-=' * 17)
print('BEM VINDO AO CONTROLE DE COMPRAS')
print('-=' * 17)
total = acima1000 = menorvalor = cont = 0
prodbarato = ''
while True:
    produto = str(input('Produto: '))
    valor = float(input('Preço: R$'))
    cont += 1
    print('-' * 20)
    total += valor
    if cont == 1:
        menorvalor = valor
    if valor <= menorvalor:
        menorvalor = valor
        prodbarato = produto
    if valor >= 1000:
        acima1000 += 1
    opção = ' '
    while opção not in 'SN':
        opção = str(input('Quer continuar: [S/N] ')).upper().split()[0]
    if opção == 'N':
        break
    print('-' * 20)
print('{:-^40}'.format('FIM DO PROGRAMA'))
print(f'O total da compra foi de {total:.2f}')
print(f'Produtos acima de R$1000,00: {acima1000}')
print(f'Produto mais barato foi {prodbarato} que custa R${menorvalor:.2f}')

