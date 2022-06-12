def titulo(texto):
    print('=' * 50)
    print(f'{texto:^50}')
    print('=' * 50)

def escreva(mensagem):
    tamanho = len(mensagem) + 4
    print('-' * tamanho)
    print(f'  {mensagem}  ')
    print('-' * tamanho)    


#  PROGRAMA PRINCIPAL
titulo('EX097 - 097 - Um print especial')

escreva('Jorge Willian')
escreva('Cusro de Python no Youtube')
escreva('CeV')
