def notas(* nota, sit=False):
    """
    -> Função usada para analisar notas e situação de vários alunos
    :param n: uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação
    :return: retorna um dicionário contendo o total de notas, maior nota, menor nota, 
    média e situação (se selecionado)
    """

    dados = {}
    
    media = sum(nota) / len(nota)

    dados['total'] = len(nota)
    dados['maior'] = max(nota)
    dados['menor'] = min(nota)
    dados['media'] = media

    if sit == True:
        if media >= 7:
            dados['situação'] = 'BOA'
        elif media >= 5:
            dados['situação'] = 'RAZOAVEL'
        else:
            dados['situação'] = 'RUIM'
    
    return dados


# Programa Principal
print(f'''{"=" * 50}
{"EX105 - Analisando e gerando Dicionários":^50}
{"=" * 50}''')

alunos = notas(5.5, 8.5, 10, 6.5, 8.5, sit=True)
print(alunos)
help(notas)

