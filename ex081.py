print(f'''{"="*50}
{"EX081 - EXTRAINDO DADOS DE UMA LISTA":^50}
{"="*50}''')

option = 'S'
numbers = []

while option == 'S':
    numbers.append(int(input('Digite um número: ')))
    option = input('Deseja continuar [S/N]? ').upper().strip()

    while option not in "SN":
        print('Opção inválida, digite novamente!')
        option = input('Deseja continuar? ').upper().strip()

    if option == 'N':
        break

print('=-'*25)
print(f'Você digitou {len(numbers)} elementos.')
print(f'Os valores em ordem decrescente são {sorted(numbers, reverse=True)}')

if 5 in numbers:
    print(f'O valor 5 faz parte da lista!')
else:
    print('O valor 5 não faz parte da lista!')
