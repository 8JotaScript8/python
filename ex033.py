'''a = int(input('digite o primeiro número:'))
b = int(input('digite o segundo número:'))
c = int(input('digite o terceiro número:'))
menor = a
if b<a and b<c:
    menor = b
if c<a and c<b:
    menor = c
maior = a
if b>a and b>c:
    maior = b
if c>a and c>b:
    maior = c
print(f'O maior é o {maior}')
print(f'o menor é o {menor}')'''

#outro jeito de fzr mais facil:
a = int(input('n1:'))
b = int(input('n2:'))
c = int(input('n3:'))
print(f'o maior numero é {max(a,b,c)}')
print(f'o menor numero é {min(a,b,c)}')

