print(f'''{"=" * 50}
{"EX 090 - Dicionário em Python":^50}
{"=" * 50}''')

aluno = {}

aluno['Nome'] = str(input('Nome do aluno: '))
aluno['Média'] = float(input('Média do aluno: '))

if aluno['Média'] >= 7:
    aluno['Situação'] = str('Aprovado')
elif aluno['Média'] >= 5 and aluno['Média'] < 7:
    aluno['Situação'] = str('Recuperação')
else:
    aluno['Situação'] = str('Reprovado')

for key, values in aluno.items():
    print(f'{key} do aluno é igual a {values}')
