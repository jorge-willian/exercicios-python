print('=-'*25)
print(f'{"ANÁLISE DE EMPRÉSTIMO":^50}')
print('=-'*25)
valor_casa = float(input('Valor da casa a financiar: '))
salario_comprador = float(input('Valor do salário do comprador: '))
anos_financiamento = int(input('Anos a pagar: '))
valor_parcelas = valor_casa / (anos_financiamento * 12)
parcelas_salario = (valor_parcelas / salario_comprador) * 100
if parcelas_salario <= 30:
    print('\n\33[1;32mFINANCIAMENTO APROVADO!\n\n\33[m'
    f'O valor da casa é de R$ {valor_casa:.2f}\n'
    f'O tempo de financiamento é de {anos_financiamento * 12} meses\n'
    f'O valor das parcelas serão de R$ {valor_parcelas:.2f}\n'
    f'As parcelas comprometem {parcelas_salario:.2f}% do salário do comprador.')
else:
    print('\n\33[1;31mFINANCIAMENTO NEGADO\n\n\33[m'
    f'O valor das parcelas excedeu 30% do valor das parcelas\n'
    f'O valor das parcelas comprometem {parcelas_salario:.2f}% do salário do comprador')
print('\n'
    f'{" FIM ":-=^25}')
