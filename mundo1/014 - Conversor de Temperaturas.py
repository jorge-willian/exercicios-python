title = ' Converter Temperatura '
print(f'{title:*^50}')

temp = float(input('Digite a temperatura em ºC: '))
faren = ((9 * temp) / 5) + 32
print(f'A temperatura de {temp:.1f}ºC corresponde a {faren:.1f}')
