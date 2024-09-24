lista =[]
c = 0
while True:
    c += 1
    n = int(input(f'Digite o {c}ª número:'))
    if n in lista:
        print('Número já registrado. Não será contabilizado')
    else:
        lista.append(n)

    while True:
        opcao = str(input('Quer continuar? [S/N]:')).strip().upper()
        if opcao == 'S' or opcao == 'N':
            break
        else:
            print("Por favor, responda apenas com 'S' para Sim ou 'N' para Não.")

    if opcao == 'N':
        break

print(lista)