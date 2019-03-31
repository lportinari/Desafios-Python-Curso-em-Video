"""
Faça um programa que jogue par ou impar com o computador. O jogo só será interrompido quando o jogador perder,
mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
"""

from random import randint
from time import sleep
print('-=' * 10)
print('JOGO DO PAR OU ÍMPAR')
print('-=' * 10)
cont = 0
while True:
    jogador = int(input('Diga um valor: '))
    escolha = str(input('PAR ou ÍMPAR [P/I]: ')).upper().split()[0]
    print('-' * 20)
    computador = randint(0, 10)
    soma = computador + jogador
    print('PAR...')
    sleep(1)
    print('OU...')
    sleep(1)
    print('ÍMPAR!!!')
    if soma % 2 == 0:
        print(f'Você jogou {jogador} e o computador {computador}, total de {soma} DEU PAR.')
        if escolha != 'P':
            print('VOCÊ PERDEU!')
            break
    else:
        print(f'Você jogou {jogador} e o computador {computador}, total de {soma} DEU ÍMPAR.')
        if escolha != 'I':
            print('VOCÊ PERDEU!')
            break
    print('-' * 20)
    print('VOCÊ VENCEU!')
    print('Vamos jogar novamente...')
    print('-=' * 10)
    cont += 1
print(f'GAME OVER! Você venceu {cont} vez(es).')






