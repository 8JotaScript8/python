def LeiaValor(msg):
    valido = False
    while not valido:
        valor = str(input((msg))).replace(',','.').strip()
        if valor.isalpha() or valor == '':
            print('\033[31mERRO! DIGITE UM VALOR VALIDO.\033[m')
        else:
            valido = True
            return float(valor)

