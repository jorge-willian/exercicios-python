print(f'''{"="*50}
{"EX084 - LISTA COMPOSTA E ANÁLISE DE DADOS":^50}
{"="*50}''')

all = []
people = []
max = min = 0


while True:
    people.append(str(input('Nome: ')))
    people.append(float(input('Peso: ')))

    if len(all) == 0:
        max = min = people[1]
    else:
        if people[1] > max:
            max = people[1]
        if people[1] < min:
            min = people[1]

    all.append(people[:])
    people.clear()

    option = input('Quer continuar? [S/N]: ')

    if option in 'Nn':
        break


print(f'O número de pessoas cadastradas foi {len(all)}')
print(f'O maior peso cadastrado foi {max} Kg. Peso de ', end='')

for p in all:
    if p[1] == max:
        print(f'{p[0]}', end=' ')


print(f'\nO menor peso cadastrado foi {min} Kg. Peso de ', end='')

for p in all:
    if p[1] == min:
        print(f'{p[0]}', end=' ')
