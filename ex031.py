d = float(input('Qual é a distancia da viajem?'))
if d>=200:
    print(f'Viajens de até 200km ou mais tem uma promoção! Sua passagem custará R${(d-200)*0.45:.2f}')
else:
    print(f'Sua passagem custará R${(200-d)*0.50:.2f}')