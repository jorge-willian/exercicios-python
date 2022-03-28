print(f'{" CAMPEONATO BRASILEIRO FEMININO ":=^50}')

times = ('Internacional','Ferroviária','Flamengo','São Paulo','Corinthians','Palmeiras','Santos','Real Brasilia','São José SP','Grêmio','Cruzeiro','Atlético MG','Avaí','Bragantino','Cresspom','Esmac')

print('=-'*50)
print(f'Os 5 primeiros colocados são {times[0:5]}')
print('=-'*50)
print(f'Os 4 últimos colocados são {times[-4::]}')
print('=-'*50)
print(f'Os times em ordem alfabética são {sorted(times)}')
print('=-'*50)
print(f'O Grêmio está na {times.index("Grêmio") + 1}ª posição')
print('=-'*50)