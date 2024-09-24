nome = str(input('qual é seu nome?')).strip()
print(f'analisando seu nome...'f'seu nome em maiusculo é {nome.upper()}\n'
      f'seu nome em minusculo é {nome.lower()}\n'
      f'seu nome possui {len(nome) - nome.count(' ')} caracteres')
lista = (nome.split())
print(f'seu primeiro nome é {lista[0]} e ele tem {len(lista[0])} letra')
