'''
Exercício Python 004: Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as
informações possíveis sobre ele.
'''

n = input('Digite algo e descubra o que é: ')
print('O tipo primitivo é:', type(n))
print('É um alphanumérico:', n.isalpha())
print('Tem letras minusculas?', n.isspace())
print('Tem letras maiusculas?', n.isupper())
print('É número?', n.isnumeric())
print('É espaço?', n.isspace())



