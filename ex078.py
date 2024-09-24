lista = []
for c in range(0,5):
    valores = int(input(f'Digite o {c+1}ª valor:'))
    lista.append(valores)
print(f'Vc digitou os números : {lista}')
print(f'O maior número digitado foi o {max(lista)} na posição {lista.index(max(lista))+1}')
print(f'O menor número digitado foi o {min(lista)} na posição {lista.index(min(lista))+1}')

