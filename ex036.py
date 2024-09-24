preco = int(input('Qual é o valor da casa? '))
salario = int(input('Qual é o seu salário? '))
anos = int(input('Em quantos anos pretende pagar esta casa? '))
parcela = preco / (anos * 12)  # Convertendo anos em meses
limite_parcela = 30 / 100 * salario

if parcela > limite_parcela:
    print(f'Com a casa sendo R${preco}, em {anos} anos, a parcela ficará em torno de R${parcela:.2f}\n'
          f'\033[31mEmpréstimo NEGADO.\033[m')  # Vermelho
else:
    print(f'Com a casa sendo R${preco}, em {anos} anos, a parcela ficará em torno de R${parcela:.2f}\n'
          f'\033[32mEmpréstimo CONCEDIDO.\033[m')  # Verde
