'''
Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e
todos os dicionários em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas
B) A média de idade
C) Uma lista com as mulheres
D) Uma lista de pessoas com idade acima da média
'''

dados = dict()
lista = list()
media = soma = 0
while True:
    dados.clear()
    dados['Nome'] = str(input('Nome: '))
    while True:
        dados['Sexo'] = str(input('Sexo [M/F]: ')).upper()[0]
        if dados['Sexo'] in 'FM':
            break
        print('ERRO! Por favor, digite apenas M ou F.')
    dados['Idade'] = int(input('Idade: '))
    soma += dados['Idade']
    lista.append(dados.copy())
    while True:
        resp = str(input('Quer continuar? [S/N]: ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resp in 'N':
        break
media = soma / len(lista)
print('-=' * 30)
print(f'A) Ao todo foram cadastrado {len(lista)} pessoas.')
print(f'B) A média de idade é {media:.2f} anos.')
print(f'C) As mulheres cadastradas são: ',end='')
for m in lista:
    if m['Sexo'] == 'F':
        print(m['Nome'], end=' ')
print()
print('D) A lista de pessoas que estão acima da média são: ')
for p in lista:
    if p['Idade'] > media:
        print('     ', end='')
        for k, v in p.items():
            print(f'{k} = {v};', end=' ')
        print()
print('<< ENCERRADO >>')




