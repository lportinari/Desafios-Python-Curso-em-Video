"""
Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa mostre:
-A media de idade do grupo
-Qual é o nome do homem mais velho
-Quntas mulheres tem menos de 20 anos
"""

import os

nomes = [] # Armazena os nomes das pessoas
idades = [] # Armazena as idades das pessoas
sexos = [] # Armazena os sexos das pessoas
soma = 0 # Soma as idades das pessoas
maisVelho = 0 # Armazena a idade do homem mais velho
nomeM = '' # Concatena nome e idade do homem mais velho
mSub20 = 0 # Armazena a quantidade de mulheres com idades abaixo de 20 anos
nomeF = '' # Concatena nome e idade das mulheres abaixo de 20 anos
for i in range(0, 4):
    print(str(i+1) + 'ª' + ' pessoa: ')
    nomes.append(input('Nome: ').capitalize())
    idades.append(int(input('Idade: ')))
    sexos.append(input('Sexo(M/F): ').upper())
    soma += idades[i]
    if sexos[i] == 'F' and idades[i] < 20:
        nomeF += nomes[i] + ',' + str(idades[i]) + ' anos; '
        mSub20 += 1

for i in range(0, len(idades)):
    if sexos[i] == 'M' and idades[i] > maisVelho:
        maisVelho = idades[i]
        nomeM = nomes[i]
print('Média de idade do grupo: {:.2f} anos.'.format(soma/4))
print('Homem mais velho: {}, {} anos.'.format(nomeM, maisVelho))
print('Mulheres acima de 20 anos: {}. {}'.format(mSub20, nomeF))

