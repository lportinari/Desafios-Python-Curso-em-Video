'''
Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular
(largura e comprimento) e mostre a área do terreno.
'''


def calcArea(larg, comp):
    area = larg * comp
    print(f'A área de um terreno {larg}x{comp} é de {area:.2f}m².')


#Programa principal
print('Controle de terrenos')
print('-' * 20)
largura = float(input('Largura [m]: '))
comprimento = float(input('Comprimento [m]: '))
calcArea(largura, comprimento)