lista = []
par = []
impar = []
for c in range(0,7):
    n = int(input(f'Digite o {c+1}ª número: '))
    lista.append(n)
    if n % 2 == 0:
        par.append(n)
    elif n % 2 != 0:
        impar.append(n)
print(f'Lista registrada: {lista}')
print(f'Registro dos números pares: {par}')
print(f'Registro dos números ímpares: {impar}')