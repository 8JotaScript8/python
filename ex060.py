'''n = int(input('Digite um valor:'))
c = n
f = 1
while c > 0:
    f *= c
    print(c if c > 0 else 1, end ='')
    if c > 1:
        print('x', end='')
    c -= 1
print(f'= {f}')'''

from math import factorial
n = int(input('Digite um número:'))
f = factorial(n)
print(f'O fatorial de {n} é {f}')


