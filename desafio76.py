"""
Exercício Python 076: Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços,
na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular.
"""

lista = ('Televisão', 2750, 'Placa de Vídeo', 1350, 'Monitor', 755, 'Mouse', 78.99, 'Teclado', 99.75,
         'Processador', 950, 'Memória', 457.75, 'SSD', 460)
print('='*44)
print('{:^44}'.format("LISTAGEM DE PREÇOS"))
print('='*44)
for itens in range(0, len(lista), 2):
    print('{:.<35} R${:.2f}'.format(lista[itens], lista[itens -1]))
print('='*44)