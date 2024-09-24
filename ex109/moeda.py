def metade(n=0):
    res = n/2
    return f'R${res:.2f}'.replace('.',',')

def dobro(n=0):
    res = n*2
    return f'R${res:.2f}'.replace('.', ',')

def aumentar(n=0, taxa=0):
    res = n + (n * taxa/100)
    return f'R${res:.2f}'.replace('.', ',')
