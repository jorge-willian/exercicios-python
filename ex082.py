print(f'''{"="*50}
{"EX082 - DIVIDINDO VALORES EM VÁRIAS LISTAS":^50}
{"="*50}''')

numbers = []
even_numbers = []
odd_numbers = []

option = 'S'

while option == 'S':
    numbers.append(int(input('Digite um número: ')))
    option = input('Deseja continuar? [S/N]: ').upper().strip()

    if option == 'N':
        break

    while option not in 'SN':
        print('Opção inválida! Digite novamente.')
        option = input('Deseja continuar? [S/N]').upper().strip()

for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)
    else:
        odd_numbers.append(num)
        
print('=-'*25)
print(f'''A lista completa é: {numbers}
A lista de pares é: {even_numbers}
A lista de ímpares é: {odd_numbers}''')


