print(f'''{"="*50}
{"EX086 - MATRIZ EM PYTHON":^50}
{"="*50}''')

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for line in range(0, 3):
    for column in range(0, 3):
        matriz[line][column] = int(input(f'Digite um valor para [{line}, {column}]: '))

print('=' * 50)
    
for line in range(0, 3):
    for column in range(0, 3):
        print(f'[{matriz[line][column]:^5}]', end='')
    print()
