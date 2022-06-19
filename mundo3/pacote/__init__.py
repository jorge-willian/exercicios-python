def metade(valor=0, form=False):
    novo_valor = valor / 2
    if form == True:
        return moeda(novo_valor)
    else:
        return novo_valor

    
def dobro(valor=0, form=False):
    novo_valor = valor * 2
    if form == True:
        return moeda(novo_valor)
    else:
        return novo_valor


def aumentar(valor=0, p=0, form=False):
    novo_valor = valor + ((valor * p) / 100)
    if form == True:
        return moeda(novo_valor)
    else:
        return novo_valor


def diminuir(valor=0, p=0, form=False):
    novo_valor = valor - ((valor * p) / 100)
    if form == True:
        return moeda(novo_valor)
    else:
        return novo_valor


def moeda(valor=0, moeda='RS'):
    novo_valor = (f'{moeda} {valor:.2f}'.replace('.', ','))
    return novo_valor


def resumo(valor=0, aumento=0, reducao=0):
    print(f'''{"-" * 35}
{"RESUMO DO VALOR":^35}
{"-" * 35}''')
    print(f'Preço analisado:{moeda(valor):>19}')
    print(f'Dobro do preço:{dobro(valor, True):>20}')
    print(f'Metade do preço:{metade(valor, True):>19}')
    print(f'{aumento}% de aumento:{aumentar(valor, aumento, True):>20}')
    print(f'{reducao}% de redução:{diminuir(valor, reducao, True):>20}')
