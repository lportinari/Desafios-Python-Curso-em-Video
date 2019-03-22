"""
Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade:
-Se ele ainda vai se alistar no serviço militar
-Se é a hora de se alistar
-Se já passou do tempo de alistamento
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
"""

from datetime import date
atual = date.today().year
print('''Digite o número correspondente ao seu sexo:
[ 1 ] \033[1;34mMASCULINO\033[m
[ 2 ] \033[1;31mFEMININO\033[m''')
sexo = int(input('Digite o valor correspondente ao seu SEXO: '))
if sexo == 2:
    print('\033[7;30mVocê não tem a obrigação de se alistar!\033[m')
nasc = int(input('Qual o ano de seu nascimento: '))
idade = atual - nasc
print('Quem nasceu em {} tem {} anos em 2018'.format(nasc, idade))
if idade == 18:
    print('Você deve se alistar \033[0;31mIMEDIATAMENTE\033[m')
elif idade < 18:
    saldo = 18 - idade
    print('Você ainda não completou 18 anos, ainda faltam {} anos para seu alistamento.'.format(saldo))
    ano = saldo + atual
    print('Seu alistamento será em {}'.format(ano))
elif idade > 18:
    saldo = idade - 18
    print('Você tem {} anos, deveria ter se a alistado a {} anos atrás.'.format(idade, saldo))
    ano = atual - saldo
    print('Seu alistamento foi em {}'.format(ano))






