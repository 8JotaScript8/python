matriz = []
spar = maior = scol = 0
par = []
n = 3
for i in range(n):
    linha = []
    for j in range(n):
        valor = int(input(f'Digite um valor para [{i}, {j}]: '))
        linha.append(valor)
        if valor % 2 == 0:
            par.append(valor)
            spar += valor
    matriz.append(linha)
print("Matriz digitada:")
for linha in matriz:
    print(linha)
print('-=-'*30)
print(f'A soma dos valores pares desta matriz é: {spar}')
for i in range(0, 3):
    scol += matriz[i][2]
print(f'A soma dos elementos da 3ª coluna são {scol}')
for j in range(0,3):
    if matriz[1][j] > maior or j == 0:
        maior = matriz[1][j]
print(f'O maior número da 2ª coluna é {maior}')


