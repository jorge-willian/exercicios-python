print('=' * 50)
print(f'{"EX078 - MAIOR E MENOR VALORES NA LISTA":^50}')
print('=' * 50)

numbers = []
higher = 0
lower = 0

for c in range(0, 5):
    numbers.append(int(input(f'Digite um número para a posição {c}: ')))
    if c == 0:
        higher = lower = numbers[c]
    else:
        if numbers[c] > higher:
            higher = numbers[c]
        elif numbers[c] < lower:
            lower = numbers[c]
    
print('=-' * 25)
print(f'Você digitou os valores {numbers}')

print(f'O maior valor digitado foi {higher} nas posições ', end='')
for i, v in enumerate(numbers):
    if v == higher:
        print(f'{i}.. ', end='')

print()

print(f'O menor valor digitado foi {lower} nas posições ', end='')
for i, v in enumerate(numbers):
    if v == lower:
        print(f'{i}.. ', end='')
