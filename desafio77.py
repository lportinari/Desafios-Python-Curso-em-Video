"""
Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar,
para cada palavra, quais são as suas vogais.
"""

vogais = ''
palavras = ('livro', 'jogo', 'televisao', 'computador', 'caneca', 'cafe', 'celular', 'carteira', 'penny', 'modem',
            'carro', 'predio', 'apartamento', 'carroça', 'emprego', 'selva', 'moto')
for p in palavras:
    print(f'\nNa palavra {p.upper()} temos ', end='')
    for letra in p:
        if letra in 'aeiou':
            print(letra, end=' ')

