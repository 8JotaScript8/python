import random
from time import sleep
v = random.randint(10,110)
print(f'{v}km/h')
print('PROCESSANDO VELOCIDADE...')
sleep(2)
multa = float(7.00)
if v<80:
    print('tudo certo! tenha um bom dia e dirija com cuidado.')
else:
    print(f'O senhor ta acima da velocidade recomendada de 80km/h. Como punição o sr sera multado em R${(v-80)*multa:.2f}. ')

