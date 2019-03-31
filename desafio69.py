"""
Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá
perguntar se o usuário quer ou não continuar. No final, mostre:
1 - Quantas pessoas tem mais de 18 anos.
2 - Quantos homens foram cadastrados.
3 - Quantas mulheres tem menos de 20 anos.
"""

print('-' * 20)
print('CADASTRO DE PESSOAS')
print('-' * 20)
maior18 = homens = mulhermenos20 = 0
while True:
    sexo = ' '
    stop = ' '
    idade = int(input('Idade: '))
    print('-' * 20)
    while sexo not in 'FM':
        sexo = str(input('Sexo: [M/F] ')).upper().split()[0]
    if idade >= 18:
        maior18 += 1
    if sexo == 'M':
        homens += 1
    if idade < 20 and sexo == 'F':
        mulhermenos20 += 1
    while stop not in 'SN':
        stop = str(input('Quer continuar: [S/N] ')).upper().split()[0]
    print('-' * 20)
    if stop == 'N':
        break
print('FIM DO PROGRAMA')
print(f'Total de pessoas com mais de 18 anos: {maior18}.')
print(f'Ao todo temos {homens} homen(s) cadastrados.')
print(f'E temos {mulhermenos20} mulher(es) com menos de 20 anos.')
