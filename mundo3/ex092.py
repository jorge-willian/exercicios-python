from datetime import date

print(f'''{"=" * 50}
{"EX092 - - Cadastro de Trabalhador em Python":^50}
{"=" * 50}''')

ano_atual = date.today().year
trabalhador = {}

trabalhador['nome'] = str(input('Nome: '))
ano_nasc = int(input('Ano de Nascimento: '))
trabalhador['idade'] = ano_atual - ano_nasc
trabalhador['ctps'] = int(input('Carteira de trabalho (0 não tem): '))

if trabalhador['ctps'] != 0:

    trabalhador['ano_contratacao'] = int(input('Ano de contratação: '))
    trabalhador['salario'] = str(input('Salário: R$ '))
    trabalhador['apos_tempo'] = 35 - (ano_atual - trabalhador['ano_contratacao'])
    trabalhador['apos_idade'] = trabalhador['idade'] + trabalhador['apos_tempo']
       
    print('=' * 50)

else:
    print(f'''{"=" * 50}
{"Trabalhador não possui carteira de trabalho."}''')

for key, values in trabalhador.items():
    print(f'{key} tem o valor {values}')

print(f'''{'=' * 50}
{" PROGRAMA FINALIZADO ":/^50}
{"=" * 50}''')
