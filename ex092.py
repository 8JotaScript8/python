from datetime import datetime
dados = dict()
v = dados.values()
k = dados.keys()
i = dados.items()

dados['Nome'] = str(input('Nome: '))
nasc = int(input('Ano de nasc: '))
dados['idade'] = datetime.now().year - nasc
dados['CTPS'] = int(input('Nª da Carteira de Trabalho (0 não tem): '))
if dados['CTPS'] != 0:
    dados['Ano de contratação'] = int(input('Ano de contratação: '))
    dados['Salario'] = int(input('Salario: R$ '))
    dados['Aposentadoria'] = dados['idade'] + (dados['Ano de contratação'] + 35) - datetime.now().year

print('-=-'*30)
for v, k in i:
    print(f'{v}= {k}')
