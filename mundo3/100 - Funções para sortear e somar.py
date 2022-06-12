from random import randint
from time import sleep

def sorteia(lista):    
    print('Sorteando os 5 valores da lista: ', end=' ')
    for cont in range(0, 5):
        num = randint(0, 100)
        print(num, end=' ')
        sleep(0.5)
        lista.append(num)
    print('PRONTO!')
    

def somapar(lista):
    print('-' * 50)
    print(f'Somando os valores pares de {lista} temos', end=' ')
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(soma, end='.')
    

print(f'''{"=" * 50}
{"EX099 - Funções para sortear e somar"}
{"=" * 50}''')

numeros = []
sorteia(numeros)
somapar(numeros)
