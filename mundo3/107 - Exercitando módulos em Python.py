import moeda

preco = float(input('Digite o preço: '))
print(f'A metade do valor {preco} é igual a {moeda.metade(preco)}.')
print(f'O dorbro do valor {preco} é igual a {moeda.dobro(preco)}.')
print(f'Aumentando 10% de {preco} temos {moeda.aumentar(preco, 10)}.')
print(f'Diminuindo 13% de {preco} temos {moeda.diminuir(preco, 13)}')
