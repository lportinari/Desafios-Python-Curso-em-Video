"""
A confederação nacional de natação precisa de um programa que leia o ano de nascimento de um atleta
e mostre sua categoria, de acordo com a sua idade
-Até 9 anos: Mirim
-Até 14 anos: Infantil
-Até 19 anos: Junior
-Até 20 anos: Senior
-Acima: Master
"""

print('-=' * 20)
print('Descubra sua categoria na confederação')
print('-=' * 20)

from datetime import date
atual = date.today().year
nasc = int(input('Digite seu ano de nascimento: '))
idade = atual - nasc
print('O atleta tem {} anos.'.format(idade))
if idade <= 9:
    print('Categora: \033[1;30mMirim')
elif idade <= 14:
    print('Categoria: \033[1;36mInfantil')
elif idade <= 19:
    print('Categoria: \033[1;33mJunior')
elif idade == 20:
    print('Categoria: \033[1;35mSenior')
else:
    print('Categoria: \033[1;31mMaster')

