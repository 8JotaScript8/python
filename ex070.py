produto_mais1000 = 0
nome_maisbarato = ''
preço_maisbarato = 0
c = 0
s = 0
print('-'*30)
print('LOJAS AFRICANAS')
print('-'*30)
while True:
    c += 1
    n = str(input('Nome do produto:'))
    p = float(input('Preço: R$'))
    s += p
    if p > 1000:
        produto_mais1000 += 1

    elif c == 1 or p < preço_maisbarato:
        preço_maisbarato = p
        nome_maisbarato = n

    print('-' * 30)
    while True:
        opcao = str(input('Quer prosseguir? [S/N]:')).strip().upper()
        if opcao == 'S' or opcao == 'N':
            break
        else:
            print('Por gentileza, apenas responda com S(Sim) ou N(Não).')

    if opcao == 'N':
        break
    print('-' * 30)

print(f'O total da compra foi R$ {s}')
print(f'Foram registrados {produto_mais1000} custando mais de R$ 1000.00')
print(f'O produto mais barato é {nome_maisbarato} custando apenas R$ {preço_maisbarato:.2f}')
