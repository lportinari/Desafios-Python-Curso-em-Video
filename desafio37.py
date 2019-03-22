"""
Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será
a base de conversão:
- 1 para Binario
- 2 para Octal
- 3 para Hexadecimal
"""

print('X' * 40)
print('Conversor BINARIO, OCTAL e HEXADECIMAL')
print('X' * 40)
num = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para conversão
[1] Converter para BINÁRIO
[2] Converter para OCTAL
[3] Converter para HEXADECIMAL''')
opção = int(input('Sua opção: '))
if opção == 1:
    print('{} convertido em BINÁRIO é igual a {}'.format(num, bin(num)[2:]))
elif opção == 2:
    print('{} convertido em OCTAL é igual a {}'.format(num, oct(num)[2:]))
elif opção == 3:
    print('{} convertido em HEXADECIMAL é igual a {}'.format(num, hex(num)[2:]))
else:
    print('Opção invalida, tente novamente.')


