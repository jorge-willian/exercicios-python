print(f'''{"="*50}
{" DESAFIO 071 - CAIXA ELETRÔNICO ":/^50}
{"="*50}''')

cont1 = cont10 = cont20 = cont50 = 0

saque = int(input('Digite o valor do saque: R$ '))
while saque >= 50:
    cont50 += 1
    saque -= 50
    if saque < 50:
        break
while saque >= 20:
    cont20 += 1
    saque -= 20
    if saque < 20:
        break
while saque >= 10:
    cont10 += 1
    saque -= 10
    if saque < 10:
        break
while saque >= 1:
    cont1 += 1
    saque -= 1
    if saque < 1:
        break
    
print(f'''{"="*50}
{cont50:2} cédulas de R$ 50,00
{cont20:2} cédulas de R$ 20,00
{cont10:2} cédulas de R$ 10,00
{cont1:2} cédulas de R$ 1,00
{"="*50}''')
