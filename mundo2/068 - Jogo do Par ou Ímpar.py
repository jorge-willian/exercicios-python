from random import randint

print(f'{" DESAFIO 068 - JOGO DO PAR OU IMPAR ":=^50}')

cont = 0

while True:    
    num_comp = randint(1, 11)
    num_joga = int(input('Diga um valor: '))
    par_impar = str(input('Par ou Impar? [P/I]: ')).upper()
    resultado = num_comp + num_joga
    print('='*50)
    
    if resultado % 2 == 0 and par_impar == 'P':
        print(f'{"Você VENCEU!":^50}')
        print(f'Você jogou {num_joga} e o computador jogou {num_comp}. Total: {resultado}!')
        cont += 1
    elif resultado % 2 == 1 and par_impar == 'I':
        print(f'{"Você VENCEU!":^50}')
        print(f'Você jogou {num_joga} e o computador jogou {num_comp}. Total: {resultado}!')
        cont += 1
    else:
        print(f'{"Você PERDEU!":^50}')
        print(f'Você jogou {num_joga} e o computador jogou {num_comp}. Total: {resultado}!')
        break
    print('='*50)

print('='*50)
print(f'GAME OVER! Você venceu {cont} vezes!')
