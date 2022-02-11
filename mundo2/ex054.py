from datetime import date

print(f'{" DESAFIO 054 - MAIORES DE IDADE ":/^50}')

ano = date.today().year
maior = 0
menor = 0
for n in range(1, 8):
    ano_nasc = (int(input(f'Em que ano a {n}ª pessoa nasceu?: ')))
    idade = ano - ano_nasc
    if idade >= 18:
        maior += 1
    else:
        menor += 1
print(f'''Maiores de Idade: {maior}
Menores de Idade: {menor}''')

