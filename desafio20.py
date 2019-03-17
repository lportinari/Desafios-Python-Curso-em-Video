"""
Exercício Python 020: O mesmo professor do desafio 019 quer sortear a ordem de apresentação de trabalhos dos alunos.
Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
"""

import random
a1 = str(input('Nome do primeiro aluno: '))
a2 = str(input('Nome do seg undo aluno: '))
a3 = str(input('Nome do terceiro aluno: '))
a4 = str(input('Nome do quarto aluno: '))
alunos = [a1, a2, a3, a4]
print('\033[1;34]A ordem dos sorteados são...')
random.shuffle(alunos)
print(alunos)


