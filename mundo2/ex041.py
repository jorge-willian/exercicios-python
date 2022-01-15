from datetime import date

print('='*50)
print(f'{"CLASSIFICAR ATLETA":^50} ')
print('='*50)

ano = date.today().year
ano_nasc = int(input('Digite o ano de Nascimento: '))
dif = ano - ano_nasc

if dif <= 9:
    print(f'O atleta possui {dif} anos e foi classificado como MIRIM')
elif dif <= 14:
    print(f'O atelta possui {dif} anos e foi classificado como INFANTIL.')
elif dif <= 19:
    print(f'O alteta possui {dif} anos e foi classificado como JUNIOR.')
elif dif <= 20:
    print(f'O alteta possui {dif} anos e foi classificado como SÊNIOR.')
else:
    print(f'O atleta possui {dif} anos e foi classificado como MASTER.')
print('--- FIM ---')