from time import sleep
n1 = int(input('Digite o 1ª valor:'))
n2 = int(input('Digite o 2ª valor:'))
print('=-='*10)
o = 0
while o != 5:
    print('''---------------------
    [ 1 ] Somar
    [ 2 ] Multiplicar
    [ 3 ] Maior
    [ 4 ] Novos números
    [ 5 ] Sair do programa
    ---------------------''')
    o = int(input('Qual é sua opção?'))
    if o == 1:
       s = n1+n2
       print(f'A soma desses 2 números é {s}')
    elif o == 2:
        m = n1*n2
        print(f'O produto desses 2 números é {m}')
    elif o == 3:
        print(f'O maior número é {max(n1,n2)}')
    elif o == 4:
        n1_2 = int(input('Digite um número:'))
        n2_2 = int(input('Digite outro:'))
        n1 = n1_2
        n2 = n2_2
    elif o == 0 or o > 5:
        print('Opção ínvalida. Tente novamente')
print('Finalizando...')
sleep(2)
print('Fim, volte sempre.')
