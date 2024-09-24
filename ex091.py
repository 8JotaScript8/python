import random
from time import sleep
jogadores = dict()


v = jogadores.values()
k = jogadores.keys()
i = jogadores.items()

jogadores['jogador 1'] = random.randint(1,6)
jogadores['jogador 2'] = random.randint(1,6)
jogadores['jogador 3'] = random.randint(1,6)
jogadores['jogador 4'] = random.randint(1,6)

for v,k in i:
    print(f'O {v} tirou {k}')
    sleep(1)
print('-=-'*30)
print('RANK:')

rank = sorted(jogadores.items(), key=lambda item: item[1], reverse=True)
for posicao, (k,v) in enumerate(rank, start=1):
    print(f'{posicao}ª lugar: {k} com {v}')
print('-=-'*30)
vencedor = rank[0]
print(f'Logo o vencedor é {vencedor[0]} com {vencedor[1]}')
