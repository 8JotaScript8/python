print('TERMOS DE UMA PA')
p1 = int(input('Qual é o primeiro termo?'))
r = int(input('Qual é a razão?'))
d = p1 + (11-1) * r
for c in range(p1, d , r):
    print(c, end=' - ')