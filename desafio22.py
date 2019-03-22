"""
Exercício Python 022: Crie um programa que leia o nome completo de uma pessoa e mostre:
- O nome com todas as letras maiúsculas e minúsculas.
- Quantas letras ao todo (sem considerar espaços).
- Quantas letras tem o primeiro nome.
"""

#Revisão
nome = str(input('Qual o seu nome compléto? ')).strip()
print('Analisando o seu nome...')
print('Seu \033[1;31mnome\033[m com letras maiúsculas: {}'.format(nome.upper()))
print('Letras minúsculas: {}'.format(nome.lower()))
print('Seu \033[1;31mnome\033[m contém {} letras'.format(len(nome)))
print('Seu primeiro \033[1;31mnome\033[m contém {} letras'.format(nome.find(' ')))


