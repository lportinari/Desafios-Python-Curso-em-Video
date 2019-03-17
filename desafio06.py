#Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
'''n = int(input('Fale um número? '))
do = n * 2
tr = n * 3
rq = n ** (1/2)
print('O dobro é {}, o triplo é {} e a raiz quadrada é {}'.format(do, tr, rq))'''


#Revisão
n = int(input('Digite um número e escubra o seu dobro, triplo e raiz quadrada: '))
d = n * 2
t = n * 3
r = n ** (1/2)
print('O dobro é {}'.format(d))
print('O triplo é {}'.format(t))
print('A raiz quadrada é {:.2f}'.format(r))