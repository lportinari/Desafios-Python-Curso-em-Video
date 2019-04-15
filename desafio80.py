"""
Exercício Python 080: Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma
lista, já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.
"""

lista = []
for c in range(5):
    num = int(input('Digite um valor: '))
    if c == 0 or num > lista[-1]:
        lista.append(num)
        print('Adicionado ao final da lista...')
    else:
        for i in range(len(lista)):
            if num <= lista[i]:
                lista.insert(i, num)
                print(f'Adicionado na posição {i} da lista...')
                break
print('-=' * 30)
print(f'Os valores digitados na ordem foram: {lista}')


