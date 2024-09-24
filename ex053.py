t = str(input('Digite algo:')).upper().strip()
tii = ''.join(t.split())
ti = ''
for c in t[::-1]:
    if c != ' ':
        ti += c
print(tii,end='')
if ti == tii:
    print('\nÉ um palíndromo')
else:
    print('\nNão é um palíndromo')