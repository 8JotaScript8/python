def fatorial(n,show=False):
    """
    ---> Calcular o fatorial de um número
    :param n: Número a ser calculado
    :param show: (Opcional) show=True mostra a conta, show=False não mostra a conta.
    :return: Valor do fatorial de um número 'n'
    """
    f = 1
    for c in range(n ,0, -1):
        f *= c
        if show:
            print(f'{c}', end=' x ')
    return f

print('=',fatorial(5, show = True))
#help(fatorial)
