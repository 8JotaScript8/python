def metade(n=0):
    res = n/2
    return res

def dobro(n=0):
    res = n*2
    return res

def aumentar(n=0, taxa=0):
    res = n + (n * taxa/100)
    return res

def moedas(n=0, simbolo='R$'):
    return f'{simbolo}{n:.2f}'.replace('.', ',')