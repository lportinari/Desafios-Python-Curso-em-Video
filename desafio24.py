"""
Exercício Python 024: Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO".
"""

cidade = str(input('Digite o nome da cidade: ')).strip().upper()
print('Analisando se existe o nome "\033[31mSANTO\033[m" na cidade')
print('SANTO' in cidade)




