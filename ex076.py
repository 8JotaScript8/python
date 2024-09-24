print('-=-'*20)
print(f'{'TABELA DE PREÇOS':^60}')
print('-=-'*20)
listagem = ('lapis', 1.75,
            'Borracha', 2,
            'Caderno', 15.40,
            'Estojo', 10.00)
for c in range(0, len(listagem), 2):
    print(f'{listagem[c]:<30} R${listagem[c+1]:>30.2f}')

