titulo = 'RADAR'

print('-='*25)
print(f'{titulo:^50}')
print('-='*25)

velocidade = float(input('Digite a velocidade do carro: '))
multa =  (velocidade - 80) * 7
if velocidade > 80:
    print('Seu carro foi multado!')
    print(f'O valor da multa é de R$ {multa:.2f}!')
else:
    print('Está dentro da velocidade permitida!')