def LeiaInt(msg):
    while True:
        try:
            num = int(input(msg))
        except(TypeError, ValueError):
            print('\033[31mErro, digite um número.\033[m')
            continue

        except KeyboardInterrupt:
            print('\033[31mNenhum dado inserido.\033[m')
            break

        else:
            return num

def LeiaFloat(msg):
    while True:
        try:
            num = float(input(msg))
        except(TypeError, ValueError):
            print('\033[31mErro, digite um número.\033[m')
            continue

        except KeyboardInterrupt:
            print('\033[31mNenhum dado inserido.\033[m')
            break

        else:
            return num



n1 = LeiaInt('Digite um número inteiro: ')
n2 = LeiaFloat('Digite um número real: ')
print(f'O valor inteiro digitado foi {n1}'
      f'\nO valor real digitado foi {n2}')




