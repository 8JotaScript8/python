def LeiaInt(msg):
    while True:
        try:
            num = int(input(msg))
            return num
        except(TypeError, ValueError):
            print('\033[31mErro, digite um número.\033[m')
            continue

        except KeyboardInterrupt:
            print('\033[31mNenhum dado inserido.\033[m')
            break

def linha(msg):
    print('-'*30)
    print(f'{msg}'.center(30))
    print('-'*30)

def menu(lista):
    linha('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'\033[33m{c}\033[m - \033[34m{item}\033[m')
        c += 1
    print('-'*30)
    opc = LeiaInt('Qual é a sua opção: ')
    return opc

def verificarFormato(arquivo):
    try:
        with open(arquivo, 'r') as arq:
            dados = arq.readlines()
            print('Conteúdo do arquivo:')
            for linha in dados:
                print(repr(linha))
    except FileNotFoundError:
        print('\033[31mErro: arquivo não encontrado!\033[m')