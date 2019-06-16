'''
Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma
mensagem com tamanho adaptável.
'''

def escreva(frase):
    n = len(frase) + 4
    print('~' * n)
    print(f'  {frase}')
    print('~' * n)


escreva('Luciano Vinicius')