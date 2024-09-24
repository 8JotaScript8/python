from datetime import date
a = int(input('que ano quer que eu analise? use 0 para analisar o ano atual:'))
if a == 0:
    a = date.today().year
if (a%4==0 and a%100!=0) or a%400==0:
    print(f'{a} é BISSEXTO.')
else:
    print(f'{a} não é BISSEXTO.')