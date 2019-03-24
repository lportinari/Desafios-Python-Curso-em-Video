"""
Crie um programa que leia o ano de nascimento de sete pessoas. No final mostre quantas pessoas ainda não atingiram
 a maioridade (21 anos) e quantas já são maiores.
 """

print('=-' * 20)
print('IDENTIFICADOR DE MAIORES')
print('=-' * 20)

from datetime import date
atual = date.today().year
maiores = 0
menores = 0
for c in range(1, 8):
    nascim = int(input('Digite o ano de nascimento da {}ª pessoa: '.format(c)))
    idade = atual - nascim
    if idade >= 21:
        maiores += 1
    else:
        menores += 1
print('''Das 7 pessoas, {} são maiores de 21 anos.
Foram encontradas {} pessoas com menos de 21 anos.'''.format(maiores, menores))
