pessoas =[]
dados = []
c = menor_peso = maior_peso = 0
while True:
    c += 1
    nome = str(input('Nome: '))
    peso = float(input('Peso: '))
    dados.append(nome)
    dados.append(peso)
    pessoas.append(dados[:])
    dados.clear()

    if peso > maior_peso:
        maior_peso = peso

    if c == 1 or peso < menor_peso:
        menor_peso = peso

    while True:
        opcao = str(input('Quer continuar? [S/N]: ')).strip().upper()
        if opcao == 'S' or opcao == 'N':
            break
        else:
            print('Por gentileza, responda apenas com S ou N.')

    if opcao == 'N':
        break

print(f'Foram registrados {c} pessoas')
print(f'O(s) maior(es) peso(s) resgitrado(s) foi(ram) {maior_peso}kg de ', end='')
for p in pessoas:
    if p[1] == maior_peso:
        print(f'[{p[0]}]', end='')
print(f'\nO(s) menor(es) peso(s) resgistrado(s) foi(ram) {menor_peso}kg de', end='')
for p in pessoas:
    if p[1] == menor_peso:
        print(f'[{p[0]}]', end='')



