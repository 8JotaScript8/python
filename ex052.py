n = int(input('Digite um número:'))
tot = 0
for c in range(1, n+1):
    if n%c == 0:
        print('\033[31m',end=' ')
        tot +=1
    else:
        print('\033[97m', end=' ')
    print(c, end=' ')
print(f'\n\033[mO número {n} foi divisivel {tot} vezes.')
if tot == 2:
    print('É PRIMO. Apenas divisivel por 1 e por ele mesmo')
else:
    print('Não é PRIMO')