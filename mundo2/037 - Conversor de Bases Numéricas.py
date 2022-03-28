while True:
    print('=-'*25)
    print(f'{"BINÁRIO, OCTAL E HEXADECIMAL":^50}')
    print('=-'*25)
    n = int(input('Digite um número inteiro: '))
    print(
        '\n---- MENU ----\n\n'
        '[1] Binário\n'
        '[2] Octal\n'
        '[3] Hexadecimal\n'
        '[0] Sair')
    opcao = input('Digite a opção desejada: ')
    if opcao == '0':
        print('--- Programa Finalizado ---')
        break
    if opcao == '1' or opcao == '2' or opcao == '3':
        if opcao == '1':
            print(f'\n\33[1;32mConvertido para Binário: {bin(n) [2:]}\33[m\n') #STRING fatiada e colorida
        elif opcao == '2':
            print(f'\n\33[1;32mConvertido para Octal: {oct(n) [2:]}\33[m\n') ##STRING fatiada e colorida
        elif opcao == '3':
            print(f'\n\33[1;32mConvertido para Hexadecimal: {hex(n) [2:]}\33[m\n') #STRING fatiada e colorida
    else:
        print('Opção Inválida')

