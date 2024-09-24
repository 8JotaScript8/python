import random
s = 0
c = 0
print('-'*30)
print('VAMOS JOGAR PAR OU IMPAR')
print('-'*30)
while True:
    x = random.randint(0,10)
    j = str(input('Qual é sua escolha, PAR ou ÍMPAR? [P/I]:')).strip().upper()
    n = int(input('Diga um valor:'))
    s = x + n
    if j == 'P' and s % 2 == 0:
        print(f'Você botou {n} e eu {x}. TOTAL = {s} deu PAR, você VENCEU.')
        c += 1
    elif j == 'I' and s % 2 != 0:
        print(f'Você botou {n} e eu {x}. TOTAL = {s} dei ÍMPAR, você VENCEU.')
        c += 1
    else:
        print(f'Você botou {n} e eu {x}. TOTAL = {s}. Você PERDEU.')
        if s % 2 == 0:
            print("O resultado foi PAR.")
        else:
            print("O resultado foi ÍMPAR.")
        print(f'Foram {c} vitórias seguidas até a derrota.')
        break
