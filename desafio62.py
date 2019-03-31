"""
Melhore o desafio 61, perguntando ao usuário se ele quer mostrar mais alguns termos. O programa encerra quando
 ele disser que quer mostrar 0 termos.
 """

print('Gerador de PA')
print('-=' * 10)
primeiro = int(input('Qual o primeiro termo: '))
razão = int(input('Qual a razão: '))
c = 0
s = 10
while c <= s or s != 0:
    print('{}'.format(primeiro), end=', ')
    primeiro += razão
    c += 1
    if c == s:
        s = int(input('Digite 0 para encerrar, ou a progressão que quer acrescentar: '))
        if s == 0:
            print('Encerrando...')
        else:
            c = 0
            print('{}'.format(primeiro), end=', ')
            primeiro += razão
            c += 1
print('Programa encerrado!')






