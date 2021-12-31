from random import randint
import pygame
from pygame.constants import KEYDOWN
pygame.init()

titulo = str('TENTE ADIVINHAR O NÚMERO')
print('-='*25)
print(f'{titulo:^50}')
print('-='*25)
numero_random = randint(0, 5)
numero_usuário = int(input('Digite um número entre 0 e 5: '))

if numero_random == numero_usuário:
    print(f'Parabéns você acertou, o computador pensou no número {numero_random}!')
    print('Pressione qualquer tecla para finalizar o programa')
    pygame.mixer.music.load('mizeravi.mp3')
    pygame.mixer.music.play()
    input()    
else:    
    print(f'Você errou o computador pensou no número {numero_random}!')
    print('Pressione qualquer tecla para finalizar o programa')
    pygame.mixer.music.load('errou.mp3')
    pygame.mixer.music.play()
    input()
print('--- PROGRAMA FINALIZADO ---')
