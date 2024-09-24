import random
n1 = input('primeiro nome:')
n2 = input('segundo nome:')
n3 = input('terceiro nome:')
lista = [n1 , n2 , n3]
print(f'a ordem escolida é {random.sample(lista, k=3)}')