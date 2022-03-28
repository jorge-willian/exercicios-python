titulo = ' Pintura Parede '
print(f'{titulo:/^50}','\n')

lar = float(input('Largura da parede: '))
alt = float(input('Altura da Parede: '))
area = lar * alt
tinta = area * 0.5

print(f'Sua parede te a dimensão de {lar}x{alt} e sua área é de {area}m².\n'
      f'Para pintar essa parede, você precisará de {tinta:.2f} litros de tinta.')

