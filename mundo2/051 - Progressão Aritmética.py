print(f'{" PROGRESSÃO ARITIMÉTICA ":/^50}')

pt = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
decimo = pt + (11 - 1) * razao #Fórmula para o décimo termo
for termo in range(pt, decimo, razao):
    print(termo, end=' → ')
print('FIM')
