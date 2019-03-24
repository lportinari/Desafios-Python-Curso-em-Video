"""
Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de 3 e que se encontram
no intervalo de 1 até 500.
"""

print('SOMA DE MÚLTIPLOS DE 3')
soma = 0 #Acumulador (Irá mostrar abaixo a soma de todos os números listados)
cont = 0 #Contador (Irá mostrar abaixo a quantidade números divísivel por 3)
for c in range(1, 501, 2):
    if c % 3 == 0:
        soma = soma + c #Acumulador
        cont = cont + 1 #Contador (O contador irá contar quantas vezes achou o número divísivel por 3)
print('A soma de todos os {} valores solicitados é igual a {}'.format(cont, soma))

