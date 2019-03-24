"""
Crie um programa que leia dois valores e mostre um menu na tela:
[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.
"""

from time import sleep
n1 = int(input('Digite um número inteiro: '))
n2 = int(input('Digite outro número inteiro: '))
print('-' * 15)
print('Escolha um opção:')
escolha = int(input('[1] SOMAR\n'
                    '[2] MULTIPLICAR\n'
                    '[3] MAIOR\n'
                    '[4] NOVOS NÚMEROS\n'
                    '[5] SAIR DO PROGRAMA\n'
                    'Digite a opção desejada: \n'))
while escolha != 5:
    if escolha == 1:
        somar = n1 + n2
        print('\033[1;31m{} + {} = {}\033[m'.format(n1, n2, somar))
    elif escolha == 2:
        multiplicar = n1 * n2
        print('\033[1;34m{} x {} = {}\033[m'.format(n1, n2, multiplicar))
    elif escolha == 3:
        if n1 > n2:
            print('\033[1;31m{}\033[m é maior que \033[1;36m{}\033[m.'.format(n1, n2))
        elif n2 > n1:
            print('\033[1;31m{}\033[m é maior que \033[1;36m{}\033[m.'.format(n2,n1))
        else:
            print('\033[1;31m{}\033[m e \033[1;31m{}\033[m são iguais.'.format(n1, n2))
    elif escolha == 4:
        n1 = int(input('Digite um número inteiro: '))
        n2 = int(input('Digite outro número inteiro: '))
    else:
        print('ERRO. Tente novamente.')
    escolha = int(input('Escolha outra opção: '))
print('Encerrando...')
sleep(1)
print('Programa encerrado!')




