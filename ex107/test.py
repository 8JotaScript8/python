import moeda

preço = float(input('Digite o preço: R$'))
print(f'A metade deste preço é R${moeda.metade(preço):.2f}'
      f'\nO seu dobro é R${moeda.dobro(preço):.2f}'
      f'\nAumentando 10% deste preço vale R${moeda.aumentar(preço,10):.2f}')