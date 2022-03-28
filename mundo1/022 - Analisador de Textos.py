# Minha Resolução
nome = str(input('Digite seu nome: '))
remove_espacos = len(nome.replace(' ', ''))
primeiro_nome = nome.split()
print(f'Todas em maiúsculas: {nome.upper()}')
print(f'Todas em minúsculas: {nome.lower()}')
print(f'Total de letras (sem espaços): {remove_espacos}')
print(f'Primeiro nome: {primeiro_nome[0]} e ele tem {len(primeiro_nome[0])} letras')

# Resolução do professor
name = str(input('Digite seu nome completo: ')).strip() # Remove os espaços extra antes e depois
print('Analisando seu nome...')
print(f'Seu nome em maiúsculas: {name.upper()}') # Deixa em maiúsculas
print(f'Seu nome em minúsculas: {name.lower()}') # Deixa em minusculas
print(f'Letras no nome: {(len(name) - name.count(" "))}') # Calcula a quantidade de letras - os espaços
print(f'Seu primeiro nome tem {name.find(" ")} letras') # Retorna a posição do primeiro espaço


