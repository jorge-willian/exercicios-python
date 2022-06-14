cores = (
'\033[m',
'\033[1;31m',
'\033[1;32m',
'\033[1;33m',
'\033[1;34m',
'\033[1;35m')

def mensagem(msg, cor=0):
    tamanho = len(msg) + 4

    print(cores[cor], end='')
    print(f'{"=" * tamanho}')
    print(f'  {msg}  ')
    print(f'{"=" * tamanho}')
    print(cores[0])


def ajuda(item):
    mensagem(f'Acessando o manual do comando {pesquisa}', 5)
    print(cores[4])
    help(item)
    print(cores[0])


while True:
    mensagem('Sistema de ajuda PyHelp', 2)
    pesquisa = input('Função ou biblioteca [Digite sair para encerrar]: ')
        
    if pesquisa.upper() == 'SAIR':
        break
    else:
        ajuda(pesquisa)
mensagem('Até logo', 3)
    
