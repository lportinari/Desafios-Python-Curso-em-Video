'''
Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário.
Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule e
acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
'''

from datetime import datetime
dados = dict()
while True:
    dados['Nome'] = str(input('Nome: '))
    nascimento = int(input('Ano de nascimento: '))
    dados['Idade'] = datetime.now().year - nascimento
    ctps = int(input('Carteira de trabalho [0 Não tem ]: '))
    if ctps == 0:
        break
    dados['Ctps'] = ctps
    dados['Contratação'] = int(input('Ano de contratação: '))
    dados['Salário'] = float(input('Salário: '))
    dados['Aposentadoria'] = 35 - (datetime.now().year - dados['Contratação']) + dados['Idade']
    break
print('-=' * 30)
for k, v in dados.items():
    print(f'    {k} tem o valor {v}.')