from time import sleep

print(f'''{" DESAFIO 059 - MENU DE OPÇÕES ":/^50})
Digite dois números inteiros''')
n1 = int(input('1º Número: '))
n2 = int(input('2º Número: '))
opcao = 0

while opcao != 5:

    print('''MENU DE OPÇÕES
[1] SOMAR
[2] MULTIPLICAR
[3] MAIOR
[4] NOVOS NUMEROS
[5] SAIR DO PROGRAMA''')
    opcao = int(input('>>> Digite a opção desejada: '))

    if opcao == 1:
        print(f'A soma entre {n1} e {n2} é igual a {n1 + n2}.')
    elif opcao == 2:
        print(f'O produto entre {n1} e {n2} é igual a {n1 * n2}.')
    elif opcao == 3:
        if n1 > n2:
            print(f'O número {n1} é o maior.')
        elif n1 < n2:
            print(f'O número {n2} é o maior.')
        else:
            print('Os dois números são iguais.')
    elif opcao == 4:
        n1 = int(input('1º número: '))
        n2 = int(input('2º número: '))
    elif opcao == 5:
        print('Programa finalizado.')
        break
    else:
        print('Opção inválida.')
    sleep(2)
    print('='*40)
    
