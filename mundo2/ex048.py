print(f'{" SOMA DE TODOS OS NÚMEROS ÍMPARES ":=^50}')
print(f'{" MÚLTIPLOS DE 3 DE 1 ATÉ 500 ":=^50}')

soma = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        soma += c # Acumulador
        cont += 1 # Contador
print(f'\n\33[1;32mA soma de todos os {cont} números é igual a {soma}!\33[m\n')
