n = int(input('digite um número:'))
u = n // 1 % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10
print(f'unidade:{u}\n'
      f'dezena:{d}\n'
      f'centena:{c}\n'
      f'milhar:{m}')