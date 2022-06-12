print(f'''{"=" * 50}
{"EX 093 - "}
{"=" * 50}''')

jogador = {}
gols = []

jogador['nome'] = str(input('Nome do jogador: '))

partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))

print('-' * 50)

for parida in range(0, partidas):
    gols.append(int(input(f'Quantos gols na partida {parida + 1}? ')))
    jogador['gols'] = gols.copy()

jogador['total'] = sum(gols)

print('-' * 50)

for key, value in jogador.items():
    print(f'O campo {key} tem o valor {value}.')

print('-' * 50)

print(f'O jogador {jogador["nome"]} jogou {partidas} partidas.')

for key, value in enumerate(gols):
    print(f'{"=> ":>5}Na partida {key} fez {value} gols.')
print(f'Foi um total de {jogador["total"]} gols.')
    
