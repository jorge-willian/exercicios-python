import numbers
from operator import ne


print(f'''{"="*50}
{"EX080 - LISTA ORDENADA SEM REPETIÇÕES":^50}
{"="*50}''')

numbers = []

for c in range(0, 5):
    new_item = int(input('Digite um número: '))
    if c == 0 or new_item > numbers[-1]:
        numbers.append(new_item)
        print('Adicionado ao fim da lista')
    else:
        cont = 0
        while cont < len(numbers):
            if new_item <= numbers[cont]:
                numbers.insert(cont, new_item)
                print(f'Adicionado a posição {cont}')
                break
            cont += 1
            
print(f'Os números adicionados foram {numbers}')
