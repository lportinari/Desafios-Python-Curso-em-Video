"""
Exercício Python 019: Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que
ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.
"""

import random
a1 = input('nome do primeiro aluno: ')
a2 = input('nome do segundo aluno: ')
a3 = input('nome do terceiro aluno: ')
a4 = input('nome do quarto aluno: ')
alunos = [a1, a2, a3, a4]
print('O escolhido é:', random.choice(alunos))


