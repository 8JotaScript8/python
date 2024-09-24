matriz = []
n = 3
for i in range(n):
    linha = []
    for j in range(n):
        valor = int(input(f'Digite um valor para [{i}, {j}]: '))
        linha.append(valor)
    matriz.append(linha)
print("Matriz digitada:")
for linha in matriz:
    print(linha)