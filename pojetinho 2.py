import datetime
import time

print('-=-'*30)
print('RELÓGIO DIGITAL')
print('-=-'*30)

while True:
    hora_atual = datetime.datetime.now().strftime('%H:%M:%S')
    print(hora_atual)
    time.sleep(1)








