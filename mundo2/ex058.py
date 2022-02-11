from random import randint
from time import sleep
import pygame
pygame.init()

print(f'\033[1;33m{" DESAFIO 058 - JOGO DA ADIVINHAÇÃO V2.0 ":/^50}\033[m\n')

print('O computador está vai pensar em um número entre 1 e 10')
print('Pensando', end='')
for c in range(1, 4):    
    print('.', end='')
    sleep(1)

num_pc = randint(1, 10)
num_usr = int(input('\nTente adivinhar o número: '))
cont = 1
while num_pc != num_usr:
    cont += 1
    print('\n\033[1;31mVocê errou, tente novamente.')
    pygame.mixer.music.load('errou.mp3')
    pygame.mixer.music.play()
    num_usr = int(input('Tente outro número: \033[m'))

print(f'''\033[1;32mVocê acertou!!!
O computador pensou no número {num_pc}.
Foram necessárias {cont} tentativas.\033[m''')
pygame.mixer.music.load('mizeravi.mp3')
pygame.mixer.music.play()
sleep(3)

