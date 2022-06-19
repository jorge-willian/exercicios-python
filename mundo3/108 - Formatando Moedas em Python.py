import moeda

preco = float(input('Digite o preço: R$ '))
print(f'A metade do valor {moeda.moeda(preco)} é igual a {moeda.moeda(moeda.metade(preco))}.')
print(f'O dorbro do valor {moeda.moeda(preco)} é igual a {moeda.moeda(moeda.dobro(preco))}.')
print(f'Aumentando 10% de {moeda.moeda(preco)} temos {moeda.moeda(moeda.aumentar(preco, 10))}.')
print(f'Diminuindo 13% de {moeda.moeda(preco)} temos {moeda.moeda(moeda.diminuir(preco, 13))}')
