print('~'*60)
print(f'{"DESAFIO 065 - LER NÚMEROS, MOSTRAR MÉDIA, MAIOR E MENOR "}')
print('~'*60)

opcao = 'S'
soma = cont = 0
lista_num = []

while opcao == 'S':
    num = int(input('Digite um número: '))
    opcao = str(input('Quer continuar? [S/N] ')).upper()
    soma += num
    cont += 1
    lista_num.append(num)
print(f'Você digiou {cont} números e a média é de {soma / cont:.2f}.')
print(f'O maior número digitado foi {max(lista_num)} e o menor número digitado foi {min(lista_num)}.')
