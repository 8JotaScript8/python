f = str(input('digite uma frase:')).strip().upper()
print(f'a letra A aparece {f.count('A')} vezes\n'
      f'a primeira letra A aparece na posição {f.find('A')+1}\n'
      f'a ultima vez que q a letra A aparece é na posição {f.rfind('A')}')