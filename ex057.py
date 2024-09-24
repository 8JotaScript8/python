s = str(input('Informe seu sexo [M/F]:')).strip().upper()
while s != 'M' and s != 'F':
        s = str(input('Dados ínvalidos. Tante novamente:')).strip().upper()
print('Recebemos seus dados senhor(a).')
