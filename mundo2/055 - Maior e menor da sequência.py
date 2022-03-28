print(f'{" DESAFIO 055 - MAIOR E MENOR PESO ":=^50}')

pesos = []
for c in range(0, 5):
    pesos.append(float(input('Digite o peso de cinco pessoas: ')))
print(f'O maior peso foi: {max(pesos)} Kg.')
print(f'O menor peso foi: {min(pesos)} Kg.')
