numero = str(input('Digite um número entre 1 e 9999: '))
print(f'Milhar: {numero[0]}\n'
      f'Centrena: {numero[1]}\n'
      f'Dezena: {numero[2]}\n'
      f'Unidade: {numero[3]}')

# Resolução do professor
num = int(input('Informe um número: '))
print(f'Analisando o número {num}')
print(f'Unidade: {num // 1 % 10}\n'
      f'Dezena: {num // 10 % 10}\n'
      f'Centena: {num // 100 % 10}\n'
      f'Milhar: {num // 1000 % 10}')

'''O número é dividido por 1 e depois dividido novamente por 10 e o resto da
divisão é mostrada'''