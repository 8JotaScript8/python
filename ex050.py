s = 0
cont = 0
for c in range(1,7):
   n = int(input(f'Digite {c} valor:'))
   if n % 2 == 0:
      s = s+n
      cont = cont+1
print(f'Foi informado {cont} números, nos quais, a soma vale {s}')




