from time import sleep
p = float(input('Qual é seu peso atual?'))
a = float(input('Qual é sua altura atual?'))
IMC = p/(a*a)
print('Calculando seu IMC...')
sleep(2)
if IMC < 18.5:
    print(f'({IMC:.2f}), Abaixo do peso ideal')
elif 18.5 <= IMC < 24.9:
    print(f'({IMC:.2f}), Peso ideal (parabens)')
elif 25.0 <= IMC < 29.9:
    print(f'({IMC:.2f}), Levemente acima do peso')
elif 30.0 <= IMC < 34.9:
    print(f'({IMC:.2f}), Obesidade grau 1')
elif 35.0 <= IMC < 39.9:
    print(f'({IMC:.2f}), Obesidade grau 2 (Severa)')
elif IMC >= 40.0:
    print(f'({IMC:.2f}), Obesidade grau 3 (Mórbida)')