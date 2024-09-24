registro = dict()
lista = list()
s = c = 0
while True:
    c += 1
    registro['Nome'] = str(input('Nome: '))
    registro['Sexo'] = str(input('Sexo [M/F]: ')).upper()
    registro['Idade'] = int(input('Idade: '))
    lista.append(registro)
    while True:
        opcao = str(input('Quer continuar? [S/N]: ')).upper().strip()
        if opcao == 'S' or opcao == 'N':
            break
        else:
            print('Por gentileza, só responder com S ou N.')
    if opcao == 'N':
        break