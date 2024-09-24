scouts = dict()
gols = list()
scouts['Nome'] = str(input('Nome do Jogador: '))
partidas = int(input('partidas disputadas: '))
tot = 0
for c in range(0,partidas):
    g = int(input(f'Gols na {c+1}ª partida: '))
    tot += g
    gols.append(g)
scouts['Gols'] = gols
scouts['Total de gols'] = tot
print(scouts)
print('-=-'*30)
for i, v in enumerate(scouts['Gols']):
    print(f'   ==>Na partida {i+1}, fez {v} gols.')
print(f'Foi um total de {tot} gols')
