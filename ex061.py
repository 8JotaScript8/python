print('TERMOS DE UMA PA')
p1 = int(input('Qual é o primeiro termo?'))
r = int(input('Qual é a razão?'))
d = p1 + (10-1) * r
c = p1
while c < d:
    print(c, end='-')
    c += r
print(d)