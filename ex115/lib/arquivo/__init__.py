from ex115.lib.interface import linha
from prettytable import PrettyTable

from ex115.lib.interface import linha

def arquivoExiste(nome):
    try:
        with open(nome, 'r') as arq:
            print('Arquivo encontrado')
    except FileNotFoundError:
        return False
    else:
        return True

def criarArquivo(nome):
    try:
        with open(nome, 'w') as arq:
            pass
    except Exception as erro:
        print(f'Houve um erro na criação do arquivo: {erro}')

def lerArquivos(nome):
    try:
        with open(nome, 'r') as arq:
            linha('PESSOAS REGISTRADAS')
            return arq.readlines()
    except Exception as erro:
        print(f'Erro ao ler o arquivo: {erro}')
        return []

def adicionarAoArquivo(nome, nomes, idade):
    try:
        with open(nome, 'a') as arq:
            arq.write(f'{nomes};{idade}\n')
    except Exception as erro:
        print(f'Houve um erro na escrita do arquivo: {erro}')


def mostrarDados():
    arq = 'cursoemvideo.txt'
    pessoas = lerArquivos(arq)
    if pessoas:
        linha('PESSOAS CADASTRADAS')
        for pessoa in pessoas:
            pessoa = pessoa.strip()
            if pessoa:  # Verifica se não está vazio
                dados = pessoa.split(';')
                if len(dados) == 2:
                    nome, idade = dados
                    print(f'Nome: {nome}, Idade: {idade}')
                else:
                    print(f'Linha mal formatada: {pessoa}')
    else:
        print('Nenhuma pessoa cadastrada.')