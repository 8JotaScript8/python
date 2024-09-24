def notas(*num, sit=False):
    """
    :param num: Aonde fica armazenado as notas
    :param sit: parametro opcinal. False = ele não mostra a situação("APROVADO" ou "REPROVADO"). True = ele mostra a situação.
    :return: Retorna ao dicionario 'dados', aonde todas as informações estão armazenadas.
    """
    dados = dict()
    dados['total'] = len(num)
    dados['maior'] = max(num)
    dados['menor'] = min(num)
    dados['media'] = sum(num) / dados['total']
    if sit:
        dados['media'] >= 7.0
        dados['situação'] = 'APROVADO'
    elif sit:
        dados['media'] < 7.0
        dados['situação'] = 'REPROVADO'

    return dados


rsp = notas(7.0,6.0,9.0, sit=True)
print(rsp)
