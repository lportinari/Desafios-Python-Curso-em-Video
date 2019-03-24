"""
Refaça o desafio 09, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.
"""

print('-=' * 10)
print('ALGORITMO DE TABUADA')
print('-=' * 10)
n = int(input('Escolha o número para a tabuada: '))
for c in range(0, 11):
    print(n, 'x', c, '= {}'.format(n * c))
    

