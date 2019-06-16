'''
Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa,
retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.
'''
from datetime import datetime

def voto(ano):
    idade = datetime.now().year - nasc
    print('Com {} anos: '.format(idade), end='')
    if idade < 16:
        print('NÃO VOTA')
    elif idade < 18 or idade > 65:
        print('VOTO OPCIONAL')
    else:
        print('VOTO OBRIGATÓRIO')




print('-' * 20)
nasc = int(input('Em que ano você nasceu? '))
voto(nasc)