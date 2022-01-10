from datetime import date

print('=-'*25)
print(f'{"ALISTAMENTO MILITAR":^50}')
print('=-'*25)

ano = date.today().year
ano_nasc = int(input('Digite seu ano de nascimento: '))
dif = ano - ano_nasc
ano_alist = ano_nasc + 18 

if dif < 18:
    print(f'Neste ano de {ano} você completa {dif} anos. Você deve se alistar em {ano_alist}.')
elif dif == 18:
    print(f'Neste ano de {ano} você completa {dif} anos, você deve se alistar IMEDIATAMENTE!')
else:
    print(f'Neste ano de {ano} você completa {dif} e deveria ter se alistado a {ano - ano_alist} anos.\n'
    f'Seu alistamento militar foi em {ano_alist}.')
print('--- FIM ---')