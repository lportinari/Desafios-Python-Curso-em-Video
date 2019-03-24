"""
Faça um programa que leia o sexo de uma pessoa, mas só aceite o valor "M" ou "F". Caso esteja errado,
peça a digitação novamente até ter um valor correto.
"""

print('=-' * 13)
print('Pesquisa do SEXO [M/F]')
print('=-' * 13)
sexo = str(input('informe seu sexo: [M/F] ')).upper().strip()[0]
while sexo not in 'FM':
    sexo = str(input('Dados invalidos. Digite seu sexo [M/F]: ')).upper().strip()[0]
print('Pesquisa coincluída. Seu sexo é {}.'.format(sexo))


