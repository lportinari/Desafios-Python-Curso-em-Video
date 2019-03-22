"""
Escreva um programa para aprovar um empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor
da casa, o salário do comprador e em quantos anos ele vai pagar.
Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário, ou então o empréstimo será negado.
"""

print('-=-' * 12)
print('CÁLCULE A MENSALIDADE DA SUA CASA')
print('-=-' * 12)

casa = float(input('Qual o valor da casa? R$'))
salario = float(input('Qual o seu salário? R$'))
tempo = int(input('A casa será parcelada em quantos anos? '))
prestação = casa / (tempo * 12)
if salario * 30 / 100 >= prestação:
    print('Parabéns, o seu empréstimo foi APROVADO. A parcela será de R${:.2f}.'.format(prestação))
elif salario * 30 / 100 < prestação:
    print ('Empréstimo NEGADO, a prestação da casa ficaria R${:.2f}, ultrapassando os 30% de seu salário.'.format(prestação))

