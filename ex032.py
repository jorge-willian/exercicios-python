print('=-'*25)
print(f'{str("ANO BISSEXTO"):^50}')
print('=-'*25)

ano = int(input('Digite o ano para verificar se ele é bissexto: '))
if (ano % 4 == 0):
    print(f'O ano {ano} é bissexto.')
else:
    print(f'O ano {ano} não é bissexto.')