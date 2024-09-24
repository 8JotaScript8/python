import random
from time import sleep
lista = ['pedra', 'papel', 'tesoura']
o = random.choice(lista)
print('-=-'*20)
print('Vamos jogar JOKENPO?')
print('-=-'*20)
print('''Suas opções:
  Pedra
  Papel
  Tesoura''')
j = str(input('Qual é sua jogada?')).strip().lower()
print('\033[1;33mJO\033[m')
sleep(1)
print('\033[1;33mKEN\033[m')
sleep(1)
print('\033[1;33mPO!!!\033[m')
print(o)
if j == o:
    print('EMPATE')
elif(j == 'papel' and o == 'pedra' or j == 'pedra' and o == 'tesoura'):
    print('\033[1;32mVC GANHOU\033[m')
else:
    print('\033[1;31mVC PERDEU\033[m')
