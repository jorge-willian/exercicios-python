print(f'{" DESAFIO 070 - ESTATÍSTICAS EM PRODUTOS ":=^50}')

soma = cont1000 = cont = menor = 0
barato = ' '

while True:
    prod = str(input('Digite o nome do produto: '))
    preco = float(input('Digite o preco do produto: '))
    cont += 1
    opcao = ' '
  
    soma += preco
    if preco > 1000:
        cont1000 += 1
    if cont == 1 or preco < menor:
        menor = preco
        barato = prod
       
    while opcao not in 'SN':
        opcao = str(input('Deseja continuar? [S/N]: ')).strip().upper()
    print('='*50)
    if opcao == 'N':
        break
    
print(f'''O total gasto na compra foi de R$ {soma:.2f}.
De todos os produtos, {cont1000} custam mais de R$ 1000,000
O produto mais barato é o (a) {barato.upper()} que custa R$ {menor:.2f}.''')
    
    

