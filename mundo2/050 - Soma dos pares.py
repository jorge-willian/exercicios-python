print(f'{" SOMANDO NÚMEROS PARES ":=^50}')

cont = 0
soma = 0
for c in range(1, 7):
    n = int(input(f'Digite o {c}º número: '))
    if n % 2 == 0:
        soma += n
        cont += 1
if cont > 1:
    print(f'''\nRESULTADO
Você informou {cont} números pares a a soma deles é de {soma}!''')
elif cont == 1:
    print(f'''\nRESULTADO
Você informou {cont} número par e o valor dele é {soma}!''')
else:
    print(f'''\nRESULTADO
Você não informou nenhum número par.''')
