print('=-'*25)
print(f'{" FORMA DE PAGAMENTO ":/^50}')
print('=-'*25)

valor_item = float(input('Digite o valor do item R$: '))
forma_pgto = int(input('\nSelecione a forma de pagamento:\n'
'[1] A vista com 10% de desconto\n'
'[2] A vista no cartão com 5% de descnto\n'
'[3] Em 2x no cartão sem juros\n'
'[4] Em três vezes ou mais com acréscimo de 20%\n'
'Digite a opção correspondente: '))

if forma_pgto == 1:
    print(f'Pagamento a vista com 10% de desconto.\n'
    f'Valor do item: R$ {valor_item}\n'
    f'Valor do item com desconto: R$ {valor_item * 0.90:.2f}')
elif forma_pgto == 2:
    print(f'Pagamento a vista no cartão com 5% de desconto.\n'
    f'Valor do produto R$ {valor_item}.\n'
    f'Valor do produto com 5% de desconto R$: {valor_item * 0.95:.2f}.')
elif forma_pgto == 3:
    print(f'Em 2x no cartão sem juros.\n'
    f'Valor do produto R$: {valor_item}\n'
    f'Valor das parcelas R$: {valor_item / 2:.2f}')
elif forma_pgto == 4:
    print(f'Em 3x ou mais com acréscimo de 20% de juros.')
    parcelas = int(input('Digite a quatidade de parcelas: '))
    print(f'Valor do produto R$: {valor_item}\n'
    f'Valor do item com acréscimo R$ {valor_item * 1.20}\n'
    f'Valor das parcelas R$ {(valor_item * 1.20) / parcelas:.2f}')
else:
    print('Opção inválida!')
