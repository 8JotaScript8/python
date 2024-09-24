import moeda

preço = float(input('Digite o preço: R$'))
print(f'A metade deste preço é {moeda.moedas(moeda.metade(preço))}'
      f'\nO seu dobro é {moeda.moedas(moeda.dobro(preço))}'
      f'\nAumentando 10% deste preço vale {moeda.moedas(moeda.aumentar(preço, 10))}')
