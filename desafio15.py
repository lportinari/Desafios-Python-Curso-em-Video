"""
Exercício Python 015: Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a
quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e
R$0,15 por Km rodado.
"""

#Revisão
dias = int(input('Qual a quantidade de dias que o carro foi alugado? '))
km = float(input('Quantos kms percorrido? '))
p = (dias * 60) + (0.15 * km)
print('Você alugou o carro por {} dia(s) e a quantidade de kms rodado foram {:.2f}'.format(dias, km))
print('O custo total da locação é de R${:.2f}'.format(p))


