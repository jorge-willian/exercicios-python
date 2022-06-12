from random import randint
from time import sleep

print(f'''{"=" * 50}
{"EX088 - PALPITES PARA A MEGA SENA":^50}
{"=" * 50}''')

jogos = []
jogo = []
cont_dezena = 6
qtd_jogos = int(input('Quantos jogos deseja sortear? '))

for game in range(0, qtd_jogos):
    while True:
        num = randint(1, 60)
        if num not in jogo:
            jogo.append(num)
            cont_dezena -= 1
        if cont_dezena == 0:
            break
    cont_dezena = 6        
    
    jogos.append(jogo[:])
    jogo.clear()

print(f'{"-" * 15}', f'SORTEANDO {len(jogos)} JOGOS', f'{"-" * 15}')

for sorteados in range(0, len(jogos)):
    print(f'Jogo {sorteados + 1}: {sorted(jogos[sorteados])}')
    sleep(1)

print(f'{" BOA SORTE ":-^50}')
