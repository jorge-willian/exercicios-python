print('-='*25)
print(f'{str("PAR OU IMPAR"):^50}')
print(f'-='*25)

numero = float(input('Digite um número: '))
divisao = numero % 2
if divisao == 0:
    print('Número Par!')
else:
    print('Número Ímpar!')
print('--- FIM ---')
