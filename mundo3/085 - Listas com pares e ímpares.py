print(f'''{"=" * 50}
{"EX085 - LISTAS COM PARES E ÍMPARES":^50}
{"=" * 50}''')

numbers = [[], []]

for n in range(1, 8):
    item = int(input(f'Digite um número para a {n}ª posição: '))
    if item % 2 == 0:
        numbers[0].append(item)
    else:
        numbers[1].append(item)

print(f'Os numeros pares digitados foram: {sorted(numbers[0])}')
print(f'Os números ímpares digitados foram: {sorted(numbers[1])}')
