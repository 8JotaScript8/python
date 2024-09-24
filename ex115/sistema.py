from ex115.lib.interface import *
from ex115.lib.arquivo import *
from prettytable import PrettyTable



arq = 'cursoemvideo.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)


while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar pessoas', 'Sair do programa'])
    if resposta == 1:
        linha('PESSOAS CADASTRADAS')
        mostrarDados()

    elif resposta == 2:
        linha('OPÇÃO 2')
        nomes = str(input('Nome: ')).strip()
        idade = LeiaInt('Idade: ')
        adicionarAoArquivo(arq,nomes,idade)
    elif resposta == 3:
        linha('Até logo')
        break
    else:
        print('\033[31mDigite uma das opções\033[m')
