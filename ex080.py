lista = []
c = 0
for c in range(0,5):
    n = int(input(f'Digite o {c+1}ª número:'))
    if c == 0:
        lista.append(n)
    elif n > lista[-1]:
        lista.append(n)
    else:
        pos = 0
        while pos < len(lista):
            lista.insert(pos,n)
            break
        pos += 1
print(lista)