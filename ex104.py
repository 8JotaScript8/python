def LeiaInt():
    while True:
        número = input('Digite um número: ')
        print('-'*30)
        if número.isnumeric():
            print(f'VocÊ digitou o número {número}.')
            return int(número)
        else:
            print('\033[31mErro, digite um número.\033[m')

n = LeiaInt()



