from random import randint
from time import sleep

while True:
    print('=-'*25)
    print(f'{" JOKENPÔ ":/^50}')
    print('=-'*25)
    
    computer = randint(1, 3)
    user = int(input('Escolha entre pedra, papel e tesoura:\n'
    '[1] Pedra\n'
    '[2] Papel\n'
    '[3] Tesoura\n'
    '[0] Sair\n'
    'Digite o número referente a opção: '))

    if user == 0:
        print('-- PROGRAMA FINALIZADO --')
        break
    elif user != 0:
        sleep(1)
        if computer == 1:
            print('O computador escolheu PEDRA!')
            if user == 1:
                print('Você escoolheu PEDRA')
                print('\33[1;33mEMPATE!!\33[m')
            elif user == 2:
                print('Você escoolheu PAPEL')
                print('\33[1;32mVocê ganhou, PAPEL EMBRULHA PEDRA!!\33[m')
            elif user == 3:
                print('Você escoolheu TESOURA')
                print('\33[1;31mVocê perdeu, PEDRA QUEBRA TESOURA!!\33[m')
        elif computer == 2:
            print('O computador escolheu PAPEL!')
            if user == 1:
                print('Você escoolheu PEDRA')
                print('\33[1;31mVocê perdeu, PAPEL EMBULHA PEDRA!!\33[m')
            elif user == 2:
                print('Você escoolheu PAPEL')
                print('\33[1;33mEMPATE!!\33[m')
            elif user == 3:
                print('Você escolheu TESOURA')
                print('\33[1;32mVocê ganhou, TESOURA CORTA PAPEL!!\33[m')
        elif computer == 3:
            print('O computador escolheu TESOURA!')
            if user == 1:
                print('Você escoolheu PEDRA')
                print('\33[1;32mVocê ganhou, PEDRA QUEBRA TESOURA!!\33[m')
            elif user == 2:
                print('Você escoolheu PAPEL')
                print('\33[1;31mVocê perdeu, TESOURA CORTA PAPEL!!\33[m')
            elif user == 3:
                print('Você escoolheu TESOURA')
                print('\33[1;33mEMPATE!!\33[m')
        else:
            print('Opção Inválida')
