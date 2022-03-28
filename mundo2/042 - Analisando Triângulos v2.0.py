print('='*50)
print(f'{"RETAS EM UM TRIÂNGULO V2":^50}')
print('='*50)

r1 = float(input('Tamanho da reta 1: '))
r2 = float(input('Tamanho da reta 2: '))
r3 = float(input('Tamanho da reta 3: '))

soma1 = r1 + r2
soma2 = r1 + r3
soma3 = r2 + r3


if (soma1 > r3) and (soma2 > r2) and (soma3 > r1):
    if r1 == r2 and r1 == r3:
        print('Há possibilidade de formar um triângulo EQUILÁTERO.')
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print('Há possibilidade de formar um triângulo ISÓCELES.')
    else:
        print('Há possibilidade de formar um triângulo ESCALENO.')
else:
    print('Não há possibilidade de formar um triângulo')
print('-- fim --')
