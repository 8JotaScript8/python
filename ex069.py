c = 0
pessoas_com_mais18 = 0
mulheres_com_menos20 = 0
homens_registrados = 0
while True:
    c += 1
    print(f'---------- {c}ªREGISTRO ----------')
    i = int(input('Idade:'))
    s = str(input('Sexo [M/F]:')).strip().upper()

    if i > 18:
        pessoas_com_mais18 += 1
    if s == 'M':
        homens_registrados += 1
    if s == 'F' and i < 20 :
        mulheres_com_menos20 += 1
    print('-----------------------------------')
    while True:
        opcao = str(input('Quer continuar? [S/N]:')).strip().upper()
        if opcao == 'S' or opcao == 'N':
            break

        else:
            print("Por favor, responda apenas com 'S' para Sim ou 'N' para Não.")


    if opcao == 'N':
        break

print(f'Totais de pessoas com mais de 18 anos: {pessoas_com_mais18}')
print(f'Ao todo temos {homens_registrados} homens registrados')
print(f'Foram registradas {mulheres_com_menos20} Mulheres/Meninas com menos de 20 anos.')
