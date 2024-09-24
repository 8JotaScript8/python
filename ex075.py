n1 = int(input('Digite 1ª número:'))
n2 = int(input('Digite 2ª número:'))
n3 = int(input('Digite 3ª número:'))
n4 = int(input('Digite 4ª número:'))
n5 = int(input('Digite 5ª número:'))
t = n1, n2, n3, n4, n5
print(f'''Vc digitou os seguintes números: {t}
O número 9 aparece {t.count(9)}
Quantidade de números pares: '''  )
for n in t:
    if n % 2 == 0:
        print(n, end=' ')

if 3 in t:
    print(f'\no número 3 apareceu pela primeira vez na posição {t.index(3)+1}')
else:
    print('\nO número 3 não foi digitado nenhuma vez')
