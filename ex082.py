lista = []
pares = []
impares = []
while True:
    n = int(input('Digite um número:'))
    lista.append(n)
    if n % 2 == 0:
        pares.append(n)
    elif n % 2 != 0:
        impares.append(n)
    while True:
        opcao = str(input('Quer continuar? [S/N]:')).strip().upper()
        if opcao == 'S' or opcao == 'N':
            break
        else:
            print('Responda apenas com S ou N.')
    if opcao == 'N':
        break

print(f'Lista: {lista} ')
print(f'Pares: {pares}')
print(f'Ímpares: {impares}')

