title = ' CONVERSOR DE MEDIDAS'
print(f'{title:/^50}\n')

med = float(input('Digite uma distância em metros: '))

print(f'{med/1000} km\n'
      f'{med/100} hm\n'
      f'{med/10} dam\n'
      f'{med*10} dm\n'
      f'{med*100:.2f} cm\n'
      f'{med*1000:.2f} mm')
