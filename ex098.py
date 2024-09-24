from time import sleep
def contador(inicio, fim, passo ):
    print(f'Contando de {inicio} até {fim} de {passo} em {passo}')
    if passo > 0 and fim >= inicio:
        fim += 1
    elif passo < 0 and fim <= inicio:
        fim -= 1

    for c in range(inicio, fim, passo):
        print(c, end=' ')
        sleep(0.5)

contador(1, 10, 1)
print()
contador(10, 0, -2)

while True:
    print('\nAgora é sua vez de definir a contagem:')
    a = int(input('Inicio: '))
    b = int(input('Fim: '))
    c = int(input('Passo: '))

    if c == 0:
        print('O passo não pode ser 0')
    elif a < b and c < 0:
        print("Para contar crescentemente, o passo deve ser positivo.")
    elif a > b and c > 0:
        print("Para contar decrescentemente, o passo deve ser negativo.")
    else:
        break

contador(a, b, c)


