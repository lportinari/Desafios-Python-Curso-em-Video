'''
Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número a calcular
e outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de
cálculo do fatorial.
'''


def fatorial(f, show=False):
    fator = f
    for i in range(f-1, 0, -1):
        fator *= i




num = int(input('Digite um número: '))
fatorial(num)