def analisador(*num):
    print('-=-'*30)
    print('Analisando números...')
    cont = 0
    for c in num:
        print(c, end=' ')
        cont += 1
    if cont > 0:
        print(f'\nForam analisados {cont} números')
        print(f'O maior número analisado é {max(num)}')
    else:
        print(f'Foram analisados {cont} números\nSem elementos para analisar')
    print('-=-'*30)

analisador(1,2,3,4,5,6)
analisador(5,6,7)
analisador(8,6)
analisador(3)
analisador()
