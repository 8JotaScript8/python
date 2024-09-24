print('TERMOS DE UMA PA')
p1 = int(input('Qual é o primeiro termo?'))
r = int(input('Qual é a razão?'))
c = p1
termos_adicionais = 10

while True:
    for _ in range(termos_adicionais):
        print(c, end='-')
        c += r

    opcao = str(input('\nQuer continuar a progressão? [S/N]:')).strip().upper()
    if opcao == 'N':
        print('Programa encerrado')
        break
    elif opcao == 'S':
        termos_adicionais = int(input('Quantos termos quer adicionar?'))
    else:
        print('Opção invalida')

print(c)