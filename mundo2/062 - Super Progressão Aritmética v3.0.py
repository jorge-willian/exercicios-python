print(f'{" DESAFIO 62 - PROGRESSÃO ARITIMÉTICA V3.0 ":/^50}')

prim_termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
termos = int(input('Digite a quantidade de termos: '))

ult_termo = (prim_termo + 9) * razao + razao
cont = 0
soma = prim_termo - razao
tot_termos = 0

while termos != 0:
    tot_termos += termos
    while cont < tot_termos:
        cont += 1
        soma += razao
        print(f'{soma} → ', end='')
    print('PAUSA')
    termos = int(input('Deseja ver mais quantos termos? '))
print(f'FIM! Você visualizou {tot_termos} termos.')
