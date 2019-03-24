"""
Elabore um programe que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de
pagamento:
-À vista dinheiro / cheque: 10% de desconto
-À vista no cartão: 5% de desconto
-Em até 2x no cartão: Preço normal
-3x ou mais no cartão: 20% de juros
"""

preço = float(input('Digite o valor das compras: '))
forma = int(input('Digite a forma de pagamento\n0 - A vista no dinheiro (10% de desconto)\n'
                  '1 - A vista no cartão (5% de desconto)\n2 - Em até 2x no cartão (Preço normal)\n'
                  '3 - 3x ou mais no cartão (20% de juros)\n'))

if forma == 0:
    print('O valor do produto será: R${:.2f}'.format(preço - (10 * preço / 100)))
elif forma == 1:
    print('O valor do produto será: R${:.2f}'.format(preço - (5 * preço /100)))
elif forma == 2:
    print('O valor do produto será: R${:.2f}'.format(preço))
elif forma == 3:
    print('O valor do produto será: R${:.2f}'.format(preço + (20 * preço / 100)))

