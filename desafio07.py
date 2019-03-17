"""
Exercício Python 007: Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.
"""

print('DESCUBRA A SUA MÉDIA')
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2
print('A sua média é: {:.2f}'.format(m))
if m < 7.5:
    print('Estude mais!')
else:
    print('Parabéns e continue estudando!')
