"""
Exercício Python 028: Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o
usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário
venceu ou perdeu.
"""

from random import randint
from time import sleep  #Comando para fazer o computador dormir por alguns segundos
print('-=-' * 15)
print('::BEM VINDO AO JOGO DE ADVINHAÇÕES::')
print('-=-' * 15)
print('Vou pensar em um número entre 0 e 5, tente advinhar...')
computador = str(input('Em que número pensei? '))
sorteio = str(randint(0, 5)) #Esse comando faz o computador pensar em um número entre 0 e 5
print('PROCESSANDO...')
sleep(1.5) #Aqui eu coloco quantos segundos
print(str('O sorteado é: {}'.format(sorteio)))
if sorteio == computador:
    print('PARABÉNS, você acertou!!!')
else:
    print('Você errou, tente novamente!')



