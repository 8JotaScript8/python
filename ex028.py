import random
from time import sleep
n = random.randint(1,5)
print('-=-'*20)
print('Vou pensar em um número de 1 a 5. Tente adivinhar...')
print('-=-'*20)
x = int(input('Em que número eu pensei?'))
print('PROCESSANDO...')
sleep(3)
if x==n:
    print('\033[32mPERDI! vc ACERTOU o número.')
else:
    print('\033[31mGANHEI! vc ERROU o número.')
