print('-='*25)
print(f'{str("MAIOR E MENOR"):^50}')
print('-='*25)

n1 = int(input('Digite o 1º número: '))
n2 = int(input('Digite o 2º número: '))
n3 = int(input('Digite o 3º número: '))

menor = n1
maior = n1

if (n2 < menor):
    menor = n2
if (n3 < menor):
    menor = n3
if (n2 > maior):
    maior = n2
if (n3 > maior):
    maior = n3

print(f'O menor número é o {menor}.')
print(f'O maior número é o {maior}.')
print('--- FIM ---')