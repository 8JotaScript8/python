def pyhelp():
    from time import sleep
    print('-'*30)
    print('Sistema pyHELP'.center(30))
    print('-'*30)
    while True:
        r = (input('Função ou Biblioteca > ')).lower()
        if r == 'fim':
            print('^' * 30)
            print('ATE LOGO'.center(30))
            print('^' * 30)
            break
        print('Buscando...')
        sleep(1)
        help(r)

pyhelp()