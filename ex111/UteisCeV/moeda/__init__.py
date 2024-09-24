def metade(n=0):
    res = n/2
    return f'R${res:.2f}'.replace('.',',')

def dobro(n=0):
    res = n*2
    return f'R${res:.2f}'.replace('.', ',')

def aumentar(n=0, taxa=0):
    res = n + (n * taxa/100)
    return f'R${res:.2f}'.replace('.', ',')

def resumo(n=0):
    print('-'*30)
    print('RESUMO'.center(30))
    print('-'*30)
    print(f'Preço analisado:   R${n:.2f}'
          f'\nMetade do preço:   {metade(n)}'
          f'\nDobro do preço:    {dobro(n)}'
          f'\nAumento de 10% do preço:    {aumentar(n,10)}')
    print('-' * 30)
