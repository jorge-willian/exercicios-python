print(f'''{'='*50}
{"EX073 - TUPLAS COM TIMES DE FUTEBOL":^50}
{'='*50}''')

times = ('Corinthians','Palmeiras','Santos','Grêmio','Cruzeiro','Flamengo','Vasco',
'Chapecoense','Atlético','Botafogo','Atlético - PR','Bahia','São Paulo','Fluminense',
'Sport Recife','EC Vitória','Coritiba','Avaí','Ponte Preta','Atlético - GO')

print('=-'*25)
print(f'Os 5 primeiros colocados são {times[0:5]}')
print('=-'*25)
print(f'Os 4 últimos colocados são {times[-4:]}')
print('=-'*25)
print(f'Os times em ordem alfabética são {sorted(times)}')
print('=-'*25)
print(f'O Chapecoense está na {times.index("Chapecoense") + 1}ª posição')
print('=-'*25)
