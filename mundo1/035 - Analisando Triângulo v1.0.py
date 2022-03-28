print('=-'*25)
print(f'{str("RETAS EM TRIÂNGULO"):^50}')
print('=-'*25)

r1 = int(input('Digite o valor da reta 1: '))
r2 = int(input('Digite o valor da reta 2: '))
r3 = int(input('Digite o valor da reta 3: '))

soma1 = r1 + r2
soma2 = r1 + r3
soma3 = r2 + r3

if (soma1 > r3) and (soma2 > r2) and (soma3 > r1):
    print('Há possibilidade de construir um triângulo.')
else:
    print('Não há possibiidade de construir um triângulo.')
