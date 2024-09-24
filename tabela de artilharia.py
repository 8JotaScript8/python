from prettytable import PrettyTable

jogadores = dict()
table = PrettyTable()
table.field_names = ['Nome','Pardidas', 'Total de gols']

while True:
    nome = str(input('Nome do Jogador: '))
    scouts = {'Nome': nome, 'Gols': [], 'Total de gols': 0}
    partidas = int(input('Partidas disputadas: '))
    tot = 0
    for c in range(0,partidas):
        g = int(input(f'Gols na {c+1}ª partida: '))
        tot += g
        scouts['Gols'].append(g)
    scouts['Total de gols'] = tot

    jogadores[nome] = scouts


    while True:
        opc = str(input('Quer analisar mais jogadores? [S/N]: ')).strip().upper()
        if opc == 'S' or opc == 'N':
            break

        else:
            print("Por favor, responda apenas com 'S' para Sim ou 'N' para Não.")

    if opc == 'N':
        break

for jogador in jogadores.values():
    table.add_row([jogador['Nome'],len(jogador['Gols']),jogador['Total de gols']])
table.sortby = 'Total de gols'
table.reversesort = True

print(table)




