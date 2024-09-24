import moeda

preço = float(input('Digite o preço: R$'))
print(f'A metade deste preço é {moeda.metade(preço)}'
      f'\nO seu dobro é {moeda.dobro(preço)}'
      f'\nAumentando 10% deste preço vale {moeda.aumentar(preço, 10)}')