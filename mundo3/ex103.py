def ficha(nome='<desconhecido>', gols=0):
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato.')    

print(f'''{"=" * 50}
{"EX103 - ":^50}
{"=" * 50}''')

n = str(input('Nome do Jogador: '))
g = str(input('Gols: '))

if g.isnumeric():
    g = int(g)
else:
    g = 0

if n.strip() == '':
    ficha(gols=g)
else:
    ficha(n, g)


