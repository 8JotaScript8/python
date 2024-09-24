lista = []
for c in range(1,6):
    p = float(input(f'Peso da {c}ª pessoa:'))
    lista.append(p)
print(f'o maior peso é {max(lista)} ')
print(f'o menor peso é {min(lista )}')

