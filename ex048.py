cont = 0
s = 0
for c in range(1, 501):
    if c % 3 ==0 and c % 2 != 0:
        cont = cont + 1
        s = s+c
print(f'a soma de todos os {cont} valores solicidados é {s}')
