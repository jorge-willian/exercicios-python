print(f'{" DESAFIO 061 - PROGRESSÃO ARITIMÉTICA ":#^50}')

prim_termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
qtd_termos = int(input('Digite a quantidade de termos: '))
ult_termo = (prim_termo + (qtd_termos - 1) * razao) + razao
cont = 0
soma = prim_termo - razao

while cont != qtd_termos:
    cont += 1
    soma += razao
    print(f'{soma} → ', end='')
print('FIM')
    
