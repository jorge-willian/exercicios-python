print(f'{" NÚMEROS PRIMOS ":/^50}')

# n = int(input('Digite um número: '))
for n in range(1, 500):
    if n == 2 or n % 2 != 0 and n != 1:
        resultado = 0
        for c in range(3, 8, 2):
            if n == c or n % c != 0:
                resultado = resultado + 1
        if resultado == 3:
                print(f'\33[1;32mO número {n} é um número primo\33[m')
        # elif resultado != 3:
            print(f'O número {n} não é um número primo')
    else:
        print(f'O número {n} não é um número primo')
