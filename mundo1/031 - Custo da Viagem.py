print('-='*25)
print(f'{str("VALOR DA PASSAGEM"):^50}')
print('-='*25)

distancia = float(input('Qual a distância da viagem? '))
if distancia <= 200:
    print(f'O valor da passagem é de R$ {distancia*0.50}!')
else:
    print(f'O valor da passagem é de R$ {distancia*0.45}!')
print('--- FIM ---')
