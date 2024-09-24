soma = 0
idade_mais_velha = 0
nome_mais_velho = ''
mulheres_com_menos20 = 0
for c in range(1,6):
    print(f'---------- {c}ª PESSOA ----------')
    n = str(input('Nome:')).strip().upper()
    i = int(input('Idade:'))
    s = str(input('Sexo [M/F]:')).strip().upper()
    soma += i
    if s == 'M' and i > idade_mais_velha:
        idade_mais_velha = i
        nome_mais_velho = n
    if s == 'F' and i < 20 :
        mulheres_com_menos20 += 1

print(f'A media de idade do grupo é {soma/5}')
print(f'O nome da pessoa mais velha é {nome_mais_velho}, com seus {idade_mais_velha} anos')
print(f'Foram registradas {mulheres_com_menos20} Mulheres/Meninas com menos de 20 anos.')
