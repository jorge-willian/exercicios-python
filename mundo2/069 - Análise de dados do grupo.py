print(f'{" DESAFIO 069 - ANALISAR DADOS ":~^40}')

cont18 = cont_m = cont_f20 = 0

while True:
    print(f'''{"-"*40}
{"CADASTRE UMA PESSOA":^40}
{"-"*40}''')
    
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F]: ')).strip().upper()[0]
    opcao = ' '
    while opcao not in 'SN':
        opcao = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]  

    if idade >= 18:
        cont18 += 1
    if sexo == 'M':
        cont_m =+ 1
    if sexo == 'F' and idade < 20:
        cont_f20 += 1
    if opcao == 'N':
        break

print(f'''Total de pessoas com 18 anos ou mais: {cont18}.
Total de homens cadastrados: {cont_m}.
Total de mulheres com menos de 20 anos: {cont_f20}.''')
