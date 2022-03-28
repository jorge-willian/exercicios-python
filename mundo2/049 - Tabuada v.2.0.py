import re


from time import sleep
print(f'{" TABUADA ":=^50}')

tab = int(input('Digite a tabuada que deseja calcular: '))

for num in range(1, 11):
    print(f'{tab} X {num:2} = {num * tab}')
      
