print(f'''{"=" * 50}
{"EX095 - Aprimorando os Dicionários":^50}
{"=" * 50}''')

# LISTAS E DICIONÁRIOS 
todos = []
jogador = {}
gols = []

# CADASTRA OS JOGADORES
while True:
    jogador['nome'] = str(input('Nome: '))
    partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))

    for partida in range(0, partidas):
        gols.append(int(input(f'Quantos gols na partida {partida + 1}? ')))

    jogador['gols'] = gols.copy()
    jogador['total'] = sum(jogador['gols'])
    gols.clear()

    todos.append(jogador.copy())
    while True:
        opcao = str(input('Deseja continuar? [S/N]')).upper() [0]
        if opcao in 'SN':
            break
        print('Opção Inválida! Digite apenas S ou N.')
    
    print('-' * 50)
    if opcao in 'Nn':
        break

# MOSTRA O CABEÇALHO   
print(f'{"cod":<4}', end='')
for i in jogador.keys():    
    print(f'{i:<15}', end='')
print()

# LISTA OS JOGADORES
for key, value in enumerate(todos):
    print(f'{key:<4}', end='')
    for d in value.values():
        print(f'{str(d):<15}', end='')
    print()

print('-' * 50)

# MOSTRA OS DADOS DE CADA JOGADOR
while True:
    num_jogador = int(input('Mostrar dados de qual jogador? [999 interrompe]: '))

    if num_jogador == 999:
        break

    elif num_jogador < len(todos):
        print(f'-- LEVANTAMENTO DO JOGADOR {todos[num_jogador]["nome"]}:')
        
        for ind, gols in enumerate(todos[num_jogador]['gols']):
            print(f'Na partida {ind + 1} o jogador fez {gols} gols.')

    else:
        print('Jogador não cadastrado, tente novamente')
    
    print('-' * 50)
