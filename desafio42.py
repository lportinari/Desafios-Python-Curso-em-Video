"""
Refaça o desafio 35 dos triângulos, acrescentando o recurso de que tipo de triângulo será formado:
-Equilatero: Todos os lados iguais
-Isósceles: Dois lados iguais
-Escaleno: Todos os lados diferentes
"""

print('-=' * 15)
print('DETECTOR DE TRIANGULOS')
print('-=' * 15)

a = float(input('Digite o comprimento do primeiro lado: '))
b = float(input('Digite o comprimento do segundo lado: '))
c = float(input('Digite o comprimento do terceiro lado: '))

if a < b + c and b < a + c and c < a + b:
    print('Os segmentos acima podem formar um TRIÂNGULO', end='')
    if a == b and b == c:
        print(' \033[1;31mEQUILÁTERO\033[m.')
    elif a != b != c != a:
        print(' \033[1;32mESCALENO\033[m')
    else:
        print(' \033[1;34mISÓSCELES\033[m')
else:
    print('Os segmentos acima NÃO PODEM formar um TRIÂNGULO!')



