print('=-'*25)
print(f'{str("AUMENTO DE SALÁRIO"):^50}')
print('=-'*25)

salario = float(input('Digite o valor do saário: '))
if salario <= 1250:
    print(f'O valor do salário com aumento de 15% será de R$ {(salario * 1.15):.2f}.')
else:
    print(f'O valor do salário com aumento de 10% será de R$ {(salario * 1.10):.2f}.')
