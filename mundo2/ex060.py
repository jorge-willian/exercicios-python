from tkinter import N


print(f'{" DESAFIO 60 - FATORIAL ":/^50}')
num = int(input('Digite o número para calcular seu fatorial: '))
cont = num
fat = 1
while cont > 0:
    fat *= cont
    cont -= 1
print(f'O fatorial de {num} é igual a {fat}.')

