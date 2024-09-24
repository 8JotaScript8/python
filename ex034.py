r1 = float(input('r1:'))
r2 = float(input('r2:'))
r3 = float(input('r3:'))
if r1+r2 > r3 and r1+r3 > r2 and r2+r3 > r1:
    print('\033[1;32mPODE formar um triangulo')
else:
    print('\033[1;31mNÃO PODE formar um tringulo')