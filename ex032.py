from datetime import date

print('=-'*25)
print(f'{str("ANO BISSEXTO"):^50}')
print('=-'*25)

ano = int(input('Digite o ano para verificar se ele é bissexto (0 para ano atual): '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano {ano} é bissexto.')
else:
    print(f'O ano {ano} não é bissexto.')
