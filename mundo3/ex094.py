print(f'''{"=" * 50}
{"EX094 - ":^50}
{"=" * 50}''')

pessoa = {}
todos = []
media = soma = 0

while True:
    pessoa['nome'] = str(input('Nome: '))
    pessoa['sexo'] = str(input('Sexo [M/F]: '))
    pessoa['idade'] = int(input('Idade: '))

    todos.append(pessoa.copy())
    

    continuar = str(input('Deseja continuar? [S/N]: '))

    if continuar not in 'Ss':
        break

for cont in range(0, len(todos)):
    soma += todos[cont]['idade']

media = soma / len(todos)

print('-' * 50)
print(f'- Ao total foram cadastradas {len(todos)} pessoas.')
print(f'- A média de idade do grupo é de {media:.0f} anos.')
print(f'- As mulheres cadastradas foram: ', end='')

for cont in range(0, len(todos)):    
    if todos[cont]['sexo'] in 'Ff':
        print(todos[cont]['nome'], end=' ')

print('\n- Lista das pessoas que estão acima da média: ')

for cont in range(0, len(todos)):
    if todos[cont]['idade'] > media:
        print(f'Nome = {todos[cont]["nome"]}; sexo = {todos[cont]["sexo"]}; idade = {todos[cont]["idade"]};')
