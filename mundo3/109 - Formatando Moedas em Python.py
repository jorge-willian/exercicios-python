import moeda

preco = float(input('Digite o preço: R$ '))
print(f'A metade do valor {moeda.moeda(preco)} é igual a {moeda.metade(preco, True)}.')
print(f'O dorbro do valor {moeda.moeda(preco)} é igual a {moeda.dobro(preco, True)}.')
print(f'Aumentando 10% de {moeda.moeda(preco)} temos {moeda.aumentar(preco, 10, True)}.')
print(f'Diminuindo 13% de {moeda.moeda(preco)} temos {moeda.diminuir(preco, 13, True)}')
