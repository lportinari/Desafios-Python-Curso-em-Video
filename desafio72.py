"""
Exercício Python 072: Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso,
de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
"""

extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
           'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezeseis', 'dezesete', 'dezoito', 'dezenove', 'vinte')

while True:
    num = int(input('Escolha um número entre 0 e 20: '))
    if num < 0 or num > 20:
        print('Escolha incorreta. ', end='')
    print('Você escolheu o número {}'.format(extenso[num]))
    cont = str(input('Quer continuar? [s/n]: ')).upper().strip()[0]
    if cont == 'N':
        break
print('Fim do programa!')

