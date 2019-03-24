"""
Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
"""

frase = str(input('Digite uma frase e descubra se ela é um PALÍNDROMO: ')).strip().upper()
junto = frase.replace(' ','')
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
print('O inverso de {} é {}'.format(junto, inverso))
if junto == inverso:
    print('Esta frase é um PALÍNDROMO!')
else:
    print('esta frase NÃO É UM PALÍNDROMO!')


#Sem o comando FOR:

'''frase = str(input('Digite uma frase e descubra se ela é um PALÍNDROMO: ')).strip().upper()
junto = frase.replace(' ','')
inverso = junto[::-1]

print('O inverso de {} é {}'.format(junto, inverso))
if junto == inverso:
    print('Esta frase é um PALÍNDROMO!')
else:
    print('esta frase NÃO É UM PALÍNDROMO!')'''


