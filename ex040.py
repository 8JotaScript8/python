n1 = float(input('Primeira nota:'))
n2 = float(input('segunda nota:'))
media = (n1+n2)/2
if media >= 7.0:
    print('PARABENS, vc passou.')
elif 5.0 <= media <= 6.9:
    print('vc esta de recuperação')
elif media < 5.0:
    print('burro burro burro burro burro')