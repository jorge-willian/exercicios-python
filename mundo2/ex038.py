print('=-'*25)
print(f'{"MAIOR E MENOR":^50}')
print('=-'*25)

n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))

if n1 > n2:
    print(f'O PRIMEIRO valor é maior!')
elif n2 > n1:
    print(f'O SEGUNDO valor é maior!')
else:
    print(f'Os números {n1} e {n2} são iguais! ')
print('--- FIM ---')
