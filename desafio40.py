"""
Crie um  programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no
 final, de acordo com a media atingida
 -Média abaixo de 5.0: REPROVADO
 -Média entre 5.0 e 6.9: RECUPERAÇÃO
 - Média acima de 7.0 ou superior: APROVADO
 """

print('=' * 25)
print('=CALCULE A SUA MÉDIA=')
print('=' * 25)

N1 = float(input('Digite a primeira nota: '))
N2 = float(input('Digite a segunda nota: '))
media = (N1 + N2) / 2
print('A média entre as notas {:.1f} e {:.1f} é: {:.1f}'.format(N1, N2, media))

if media < 5.0:
    print('Você está \033[1;31m"REPROVADO"\033[m')
elif media >= 5.0 and media <= 6.9:
    print('Você está de \033[1;33m"RECUPERAÇÃO"\033[m')
elif media >= 7.0:
    print('Você está \033[1;34m"APROVADO"\033[m')