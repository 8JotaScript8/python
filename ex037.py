n = int(input('Digite um número:'))
print('''''Escolha uma das bases de converção:
[ 1 ] BINÁRIO
[ 2 ] OCTAL
[ 3 ] HEXADECIMAL''''')
opção = int(input('Sua escolha:'))
if opção == 1:
    print(f'convertido para BINÁRIO é igual a {bin(n)}'[2:])
elif opção == 2:
    print(f'covertido para OCTAL é igual a {oct(n)}'[2:])
elif opção == 3:
    print(f'convertido para HEXADECIMAL é igual a {hex(n)}'[2:])
else:
    print(f'\033[31mOpção invalida, tente novamente\033[m')
