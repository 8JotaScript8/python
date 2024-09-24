n = s = 0
c = 0
while True:
    n = int(input('Digite um valor (Para parar digite 999):'))
    if n == 999:
        break
    s += n
    c += 1
print(f'Foram registrados {c} números e a soma deles é {s}')