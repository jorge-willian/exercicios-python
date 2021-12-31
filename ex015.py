title = ' Aluguel de carros '
print(f'{title:*^50}')
dias = int(input('Por quantos dias o carro foi alugado? '))
km = float(input('Quanto KM o carro rodou? '))
total = (dias * 60) + (km * 0.15)
print(f'O valor total a pagar é de R$ {total:.2f}.')