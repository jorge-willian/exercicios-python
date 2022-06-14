def fatorial(num, show=False):
    """
    -> Faz o cálculo de fatorial
    :param num: fatorial a ser calculado
    :param show: True -> Mostra o cálculo; False (padrão) -> Não mostra o cálculo 
    Função criada por Jorge Willian de Oliveira
    """    
    if show == True:
        for cont in range(num, 1, -1):
            print(cont, 'x', end=' ')
        print(f'1', end=' = ')
    
    soma = 1
    for cont in range(num, 0, -1):
        soma *= cont
    
    return soma


print(f'''{"=" * 50}
{"EX102 - Função para fatorial":^50}
{"=" * 50}''')

print(fatorial(7, True))
help(fatorial)
