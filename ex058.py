import random
from time import sleep
cont = 0
n = random.randint(0,10)
print('-=-'*20)
print('Vou pensar em um número de 0 a 10. Tente adivinhar...')
print('-=-'*20)
x = int(input('Em que número eu pensei?'))
print('PROCESSANDO...')
sleep(3)
while n!= x:
    x = int(input('\033[1;31mErrou\033[m.Tente novamente:'))
    cont += 1
print(f'Muito bem, vc \033[1;32mGANHOU\033[m. Foram \033[1;33m{cont}\033[m tentativas até o acerto.')