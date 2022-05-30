print(f'''{"=" * 50}
{"EX087 - MAIS SOBRE MATRIZ EM PYTHON":^50}
{"=" * 50}''')

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
even_numbers = sum_col_3 = max_line_2 = 0

for line in range(0, 3):
    for column in range(0, 3):
        matriz[line][column] = int(input(f'Digite o valor para [{line}, {column}]: '))

for line in range(0, 3):
    for column in range(0, 3):
        if matriz[line][column] % 2 == 0:
            even_numbers += matriz[line][column]

for line in range(0, 3):
    sum_col_3 += matriz[line][2]

for column in range(0, 3):
    if matriz[1][column] > max_line_2:
        max_line_2 = matriz[1][column]

print('=' * 50)

for line in range(0, 3):
    for column in range(0, 3):
        print(f'[{matriz[line][column]:^5}]', end='')
    print()

print('=' * 50)

print(f'A soma de todos os números pares é igual a {even_numbers}.')
print(f'A soma dos valores da terceira coluna é igual a {sum_col_3}.')
print(f'O maior valor da segunda linha é {max_line_2}')
