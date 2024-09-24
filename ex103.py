def ficha(nome='desconhecido',gols=0):
    print('-'*30)
    print(f'O jogador {nome} fez {gols} gols.')


n = str(input('Nome do jogador: ')).strip()
g = str(input('Números de gols: '))

if g == '':
    ficha(nome=n)
elif n == '':
    ficha(gols=g)
else:
    ficha(n,g)
