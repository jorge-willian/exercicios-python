print(f'{" DESAFIO 057 - VALIDADOR DE DADOS":/^50}')

sexo = str('')
while sexo != 'M' and sexo != 'F':
    sexo = str(input('Digite seu sexo (M/F): ')).strip().upper()
    if sexo != 'M' and sexo != 'F':
        print('Opção Inválida, digite M ou F')
if sexo == 'M':
    print('Você selecionou MASCULINO')
else:
    print('Você selecionou FEMININO')

