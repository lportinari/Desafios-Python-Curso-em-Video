"""
Escreva um programa que leia 2 números inteiros e compare-os, mostrando na tela uma mensagem
- O primeiro valor é maior
- O segundo valor é maior
- Não existe valor maior, os dois são iguais
"""

print('-=-' * 14)
print('Descubra qual valor é maior')
print('-=-' * 14)

v1 = int(input('Digite um número: '))
v2 = int(input('Digite outro número: '))
if v1 > v2:
    print('\33[1;32m{}\33[m é maior que \33[1;36m{}\33[m'.format(v1,v2))
elif v2 > v1:
    print('\33[1;32m{}\33[m é maior que \33[1;36m{}\33[m'.format(v2,v1))
elif v1 == v2:
    print('Ambos os números são iguais')
