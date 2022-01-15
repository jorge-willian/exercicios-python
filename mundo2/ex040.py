print('='*50)
print(f'{"MÉDIA ARITIMÉTICA":^50}')
print('='*50)

n1 = float(input('Nota 1: '))
n2 = float(input('Nota 2: '))
med = (n1 + n2) / 2

if med < 5:
    print(f'A média do aluno é {med:.1f}, o aluno foi \33[1;31mREPROVADO!\33[m')
elif med >= 5 and med < 7:
    print(f'A média do aluno é {med:.1f}, o aluno ficou em \33[1;33mRECUPERAÇÃO!\33[m')
else:
    print(f'A média do aluno é de {med:.1f}, o aluno foi \33[1;32mAPROVADO!\33[m')
print('--- FIM ---')

