"""
Crie um programa que faça o computador jogar "Jokempô" com você
"""

from random import randint #Foi importado a opção randint para o sorteio
from time import sleep #Foi importado a animação JO KEN PÔ!!!
itens = ('Pedra', 'Papel', 'Tesoura') #Foi classificado 0 para pedra, 1 para papel e 2 para tesoura
computador = randint(0 , 2) #O computador irá escolher uma opção entre 0 e 2

print('=-=' * 10)
print('JOKEMPÔ CONTRA A MAQUINA')
print('=-=' * 10)

print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Qual a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ!!!')
print('-=' * 11)
print('Jogador jogou {}'.format(itens[jogador]))
print('Computador jogou {}'.format(itens[computador]))
print('-=' * 11)
if computador == 0: #Computador jogou Pedra
    if jogador == 0:
        print('\033[1;33mEMPATE')
    elif jogador == 1:
        print('Você \033[1;34mVENCEU')
    elif jogador == 2:
        print('Você \033[1;31mPERDEU')
    else:
        print('OPÇÃO INVALIDA')
elif computador == 1: #Computador jogou Papel
    if jogador == 0:
        print('Você \033[1;31mPERDEU')
    elif jogador == 1:
        print('\033[1;33mEMPATE')
    elif jogador == 2:
        print('Você \033[1;34mVENCEU')
    else:
        print('OPÇÃO INVALIDA')
elif computador == 2: #Compoutador jogou Tesoura
    if jogador == 0:
        print('Você \033[1;34mVENDEU')
    elif jogador == 1:
        print('Você \033[1;31mPERDEU')
    elif jogador == 2:
        print('\033[1;33mEMPATE')
    else:
        print('OPÇÃO INVALIDA')


