n1 = int(input('Digite um número:'))
n2 = int(input('Digite outro número:'))
if n1>n2:
    print(f'{n1} é maior o maior número.')
elif n2>n1:
    print(f'{n2} é o maior número.')
elif n1==n2:
    print(f'ambos tem o mesmo valor.')