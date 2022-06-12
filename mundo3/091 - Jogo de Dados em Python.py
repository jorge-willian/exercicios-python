print(f'''{"=" * 50}
{"091 - Jogo de Dados em Python":^50}
{"=" * 50}''')

from operator import itemgetter
from random import randint
from time import sleep

jogo = {
'Carlos': randint(1, 6),
'Roberto': randint(1, 6),
'José': randint(1, 6),
'Mauro': randint(1, 6)}

ranking = []

ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)

for key, values in jogo.items():
    print(f'O {key} tirou {values} no dado!')
    sleep(1)

print('-' * 50)

for ind, value in enumerate(ranking):
    print(f'{ind + 1}º Lugar: {value[0]} com {value[1]} pontos!')
    sleep(1)

print('-' * 50)






