"""
Desenvolva uma lógica que leia o peso e altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a
tabela abaixo:
-Abaixo de 18.5: Abaixo do peso
-Entre 18.5 e 25: Peso ideal
-25 até 30: Sobrepeso
-30 até 40: Obesidade
-Acima de 40: Obesidade mórbida
"""

print('-=-' * 6)
print('CALCULE SEU IMC')
print('-=-' * 6)

peso = float(input('Digite o seu peso em kg: '))
altura = float(input('Digite a sua altura: '))
imc = peso / (altura * altura)

if imc < 18.5:
    print('Seu IMC é {:.2f}: Abaixo do peso'.format(imc))
elif 18.5 <= imc < 25:
    print('Seu IMC é {:.2f}: Peso ideal'.format(imc))
elif 25 <= imc < 30:
    print('Seu IMC é {:.2f}: Sobrepeso'.format(imc))
elif 30 <= imc < 40:
    print('Seu IMC é {:.2f}: Obesidade'.format(imc))
elif imc >= 40:
    print('Seu IMC é {:.2f}: Obesidade mórbida'.format(imc))
