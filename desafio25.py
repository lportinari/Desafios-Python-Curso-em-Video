"""
Exercício Python 025: Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.
"""

print('=Identificador de "Silva" no nome=')
nome = str(input('Digite o seu nome compléto: ')).upper()
print('Seu nome é', nome)
print('Contém Silva no seu nome?', 'SILVA' in nome)