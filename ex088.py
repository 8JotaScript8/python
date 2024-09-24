import random
print('-=-'*30)
print('JOGO DA MEGA SENA'.center(85))
print('-=-'*30)
sort = int(input('Quantos jogos quer sortear? '))
for w in range(0, sort):
    lista = []
    for c in range(0,6):
        n = random.randint(1,60)
        while n in lista:
            n = random.randint(1, 60)
        lista.append(n)
    print(lista)