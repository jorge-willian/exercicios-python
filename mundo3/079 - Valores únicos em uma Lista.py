print(f'''{"="*50}
{"EX079 - VALORES ÚNICOS EM UMA LISTA":^50}
{"="*50}''')

def list_values():
    numbers.sort()
    for item in numbers:
        print(item, end=' ')

numbers = []
option = 'S'

while option == 'S':
    new_item = int(input('Digite um valor: '))
    if new_item not in numbers:
        numbers.append(new_item)
        print(f'\33[1;32mValor {new_item} adicionado com sucesso!\33[m')
    else:
        print('\33[1;31mNúmero duplicado! Não será adicionado.\33[m')

    option = input('Quer continuar? ').upper().strip()
    
    if option == 'N':
        break

    while option not in 'SN':
        print('\33[1;33mOpção Inválida, digite novamente.\33[m')
        option = input('Quer continuar [S/N]? ').upper().strip()
                       
print(f'Você adicionou os valores: ', end='')
list_values()

