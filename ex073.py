t = ('Botafogo', 'Atletico-MG', 'Bragantino', 'Athletico-PR', 'Bahia', 'Internacional', 'Cruzeiro', 'Flamengo', 'Gremio', 'Criciúma', 'Fortaleza', 'Palmeiras', 'Juventude', 'São Paulo', 'Corinthians', 'Fluminense', 'Vasco da Gama', 'Vitoria', 'Atlético-GO', 'Cuiabá')
posicao_flamengo = t.index('Flamengo') + 1
print(f'''°Lista dos times: {t}
°Os 5 primeiros colocados: {t[0:5]}
°Os 4 ultimos colocados: {t[16:20]}
°Os times em ordem alfabetica: {sorted(t)}
°A posição do Flamengo na tabela é {posicao_flamengo}ª''')

