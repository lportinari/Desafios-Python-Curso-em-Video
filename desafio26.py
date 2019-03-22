"""
Exercício Python 026: Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A", em
que posição ela aparece a primeira vez e em que posição ela aparece a última vez.
"""

frase = str(input('Digite uma frase: ')).lower()
print('A frase digitada foi :'.format(frase))
print('Analisando...')
print('Sua frase aparece a letra "\033[1;36mA\033[m" {} vezes'.format(frase.count('a')))
print('A letra "\033[1;36mA\033[m" aparece a primeira vez na posição {}'.format(frase.find('a')+1))
print('A letra "\033[1;36mA\033[m" aparece a última vez na posição {}'.format(frase.rfind('a')+1))

