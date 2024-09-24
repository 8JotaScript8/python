def voto(n):
    from datetime import date
    print('-'*30)
    ano_atual = date.today().year
    idade = ano_atual - n
    if idade < 16:
        return f'Com {idade} anos: NÃO VOTA.'
    elif 16 <= idade <18 or idade > 65:
        return f'Com {idade} anos: VOTO OPCIONAL.'
    else:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO.'


nsc = voto(int(input('Ano de nascimento: ')))
print(nsc)




