"""
Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se
a expressão passada está com os parênteses abertos e fechados na ordem correta.
"""

exp = str(input('Digite a empressão: '))
pilha = list()
for i in exp:
    if i == '(':
        pilha.append('(')
    elif i == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('A expressão está correta.')
else:
    print('A expressão está incorreta.')
