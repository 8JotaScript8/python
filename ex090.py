aluno = dict()
v = aluno.values()
k = aluno.keys()
i = aluno.items()
aluno['Nome'] = str(input('Nome do aluno: '))
aluno['Média'] = float(input('Qual é a média do aluno: '))
if aluno['Média'] < 7.0:
    aluno['Situção'] = 'Reprovado'
else:
    aluno['Situção'] = 'Aprovado'
print('-=-'*30)
for v,k in aluno.items():
    print(f'-{v}: {k} ')