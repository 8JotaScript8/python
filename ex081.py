lista = []
while True:
    n = int(input(f'Digite algum número:'))
    lista.append(n)
    while True:
        opcao = str(input('Quer continuar? [S/N]:')).strip().upper()
        if opcao == 'S' or opcao == 'N':
            break
        else:
            print('Responda apenas com S ou N.')
    if opcao == 'N':
        break
print(lista)
lista_decre = sorted(lista, reverse = True)
print(f'Lista em ordem decrescente: {lista_decre}')
print(f'O número 5 esta na lista?')
if lista.count(5) == True:
    print('Sim')
else:
    print('Não')