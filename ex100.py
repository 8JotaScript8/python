import random
def sorteador(lst):
    print('Sorteando 5 valores da lista...')
    for c in range(0,5):
        n = random.randint(0,9)
        lst.append(n)
        print(n, end=' ')

def somaPar(lst):
    soma = 0
    for valor in lst:
        if valor % 2 == 0:
            soma += valor
    print(f'\nSomando os valores pares de {lst} temos {soma}')

numeros = list()
sorteador(numeros)
somaPar(numeros)










